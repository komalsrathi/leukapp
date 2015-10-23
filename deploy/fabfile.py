"""
required packages at server:
    * nginx
    * Python 3.4
    * git
    * pip
    * virtualenv
    * virtualenvwrapper

fab commad example:

fab \
    deploy:host=medinaj@plvleukweb1.mskcc.org \
    -f fabfile.py \
    --set=VIRTUALENV=staging,REPO_URL=git@github.com:leukgen/leukapp.git,REQUIREMENTS=production.txt,DJ_SETTINGS=config.settings.staging\

"""

# third party
from fabric.contrib.files import exists  # append, sed
from fabric.api import env, local, run


def deploy():

    # settings
    user = env.user
    host = env.host
    repo = env.REPO_URL
    settings = env.DJ_SETTINGS
    virtualenv = env.VIRTUALENV
    virtualenv_folder = '/home/{0}/.virtualenvs/{1}'.format(user, virtualenv)
    site_folder = '/home/{0}/sites/{1}'.format(user, host)
    source_folder = site_folder + '/source'
    requirements = source_folder + '/requirements/' + env.REQUIREMENTS

    # deploy
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder, repo)
    _update_nginx_conf(host)
    _update_virtualenv(virtualenv, virtualenv_folder, requirements)
    _update_static_files(virtualenv, settings)
    _update_database(virtualenv, settings)


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ['source']:
        run('mkdir -p {0}/{1}'.format(site_folder, subfolder))


def _get_latest_source(source_folder, repo):
    if exists(source_folder + '/.git'):
        run('cd {0} && git fetch'.format(source_folder))
    else:
        run('git clone {0} {1}'.format(repo, source_folder))
    git = 'git reset --hard'
    current_commit = local("git log -n 1 --format=%H", capture=True)
    command = 'cd {0} && {1} {2}'.format(source_folder, git, current_commit)
    run(command)


def _update_nginx_conf(host):
    with open('./nginx.template.conf', 'r') as f:
        conf = f.read()
    conf = conf.replace("SITENAME", host)
    available = '/etc/nginx/sites-available'
    enabled = '/etc/nginx/sites-enabled'
    c1 = 'dzdo mkdir -p {0} {1}'.format(available, enabled)
    c2 = "echo '{0}' | dzdo tee {1}/{2}".format(conf, available, host)
    c3 = 'dzdo ln -sf {0}/{1} {2}/{1}'.format(available, host, enabled)
    c4 = 'dzdo service nginx restart'
    commands = [c1, c2, c3, c4]
    for command in commands:
        run(command)


def _update_virtualenv(virtualenv, virtualenv_folder, requirements):
    if not exists(virtualenv_folder):
        run('mkvirtualenv ' + virtualenv)
    workon = 'workon ' + virtualenv
    run(workon + ' && pip install -r ' + requirements)


def _update_static_files(virtualenv, settings):
    workon = 'workon ' + virtualenv
    collectstatic = workon + ' && python manage.py collectstatic --noinput'
    command = collectstatic + ' --settings=' + settings
    run(command)


def _update_database(virtualenv, settings):
    workon = 'workon ' + virtualenv
    migrate = workon + ' && python manage.py migrate --noinput'
    command = migrate + ' --settings=' + settings
    run(command)
