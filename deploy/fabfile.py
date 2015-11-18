"""
required packages at server:
    * nginx
    * Python 3.4
    * git
    * pip
    * deployment
    * virtualenvwrapper

fab commad example: deploy.sh
"""
import random

# third party
from fabric.contrib.files import exists, sed  # append
from fabric.api import env, local, run


def deploy():

    # load settings
    project_dir = env.PROJECT_DIR
    user = env.user
    host = env.host
    repo = env.REPO_URL
    settings = env.DJ_SETTINGS
    deployment = env.DEPLOYMENT
    virtualenv_folder = '/home/{0}/.virtualenvs/{1}'.format(user, deployment)
    site_folder = '/home/{0}/sites/{1}'.format(user, host)
    source_folder = site_folder + '/source'
    requirements = source_folder + '/requirements/' + env.REQUIREMENTS

    # deploy
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder, repo)
    _update_nginx_conf(host, project_dir)
    _update_virtualenv(deployment,
                       virtualenv_folder,
                       requirements,
                       source_folder)
    _update_settings(source_folder, deployment)
    _update_static_files(deployment, settings)
    _update_database(deployment, settings)
    _restart_server(host, deployment)


def _create_directory_structure_if_necessary(site_folder):
    """
    The -p setting makes directory only if necessary
    """
    for subfolder in ['source']:
        run('mkdir -p {0}/{1}'.format(site_folder, subfolder))


def _get_latest_source(source_folder, repo):
    """
    If there is no .git folder, the repo is cloned.
    Otherwise the repo fetched, and reset to the latest commit.
    """
    if exists(source_folder + '/.git'):
        run('cd {0} && git fetch'.format(source_folder))
    else:
        run('git clone {0} {1}'.format(repo, source_folder))
    git = 'git reset --hard'
    current_commit = local("git log -n 1 --format=%H", capture=True)
    command = 'cd {0} && {1} {2}'.format(source_folder, git, current_commit)
    run(command)


def _update_nginx_conf(host, project_dir):
    """
    Updates the nginx sites-available, sites-enabled files using the template
    available at /deploy/nginx.template.conf
    """
    with open(project_dir + '/deploy/nginx.template.conf', 'r') as f:
        conf = f.read()
    conf = conf.replace("HOST", host)
    available = '/etc/nginx/sites-available'
    enabled = '/etc/nginx/sites-enabled'
    c1 = 'dzdo mkdir -p {0} {1}'.format(available, enabled)
    c2 = "echo '{0}' | dzdo tee {1}/{2}".format(conf, available, host)
    c3 = 'dzdo ln -sf {0}/{1} {2}/{1}'.format(available, host, enabled)
    c4 = 'dzdo service nginx restart'
    commands = [c1, c2, c3, c4]
    for command in commands:
        run(command)


def _update_virtualenv(
        deployment, virtualenv_folder, requirements, source_folder):
    """
    Creates or updates the virtual environment. Postactivate script is also
    updated based on template found at /.env/`deployment`_postactivate
    """
    if not exists(virtualenv_folder):
        run('mkvirtualenv ' + deployment)

    postactivate = '/.env/{0}_postactivate'.format(deployment)
    postsource = source_folder + postactivate
    postvirtual = virtualenv_folder + '/bin/postactivate'
    run('ln -sf {0} {1}'.format(postsource, postvirtual))
    workon = 'workon ' + deployment
    run(workon + ' && pip install -r ' + requirements)


def _update_settings(source_folder, deployment):
    """
    Adds a randomly generated DJANGO_SECRET_KEY to the postactivate script.
    """
    postactivate = '/.env/{0}_postactivate'.format(deployment)
    postsource = source_folder + postactivate
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&'
    key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
    key = "DJANGO_SECRET_KEY={0}".format(key)
    sed(postsource, "DJANGO_SECRET_KEY=CHANGE_ME", key)


def _update_static_files(deployment, settings):
    """
    Simply updates the static files.
    """
    workon = 'workon ' + deployment
    collectstatic = workon + ' && python manage.py collectstatic --noinput'
    command = collectstatic + ' --settings=' + settings
    run(command)


def _update_database(deployment, settings):
    """
    Runs makemigrations and migrate commands.
    """
    workon = 'workon ' + deployment
    makemigrations = workon + ' && python manage.py makemigrations'
    command = makemigrations + ' --settings=' + settings
    run(command)
    migrate = workon + ' && python manage.py migrate --noinput'
    command = migrate + ' --settings=' + settings
    run(command)


def _restart_server(host, deployment):
    """
    Restarts the server.
    """
    venv = "workon {0} && ".format(deployment)
    gunicorn = "gunicorn --bind unix:/tmp/HOST.socket "
    gunicorn = gunicorn.replace("HOST", host)
    gunicorn_config = "config.wsgi:application "
    run(venv + gunicorn + gunicorn_config)
