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
    """
    Deploy project based on environment variables.
    """

    # LOAD VARIABLES
    # ---------------------------------------------------
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

    # DEPLOY
    # ---------------------------------------------------
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
    _restart_server(host, source_folder, deployment)


def _create_directory_structure_if_necessary(site_folder):
    """
    Make project directory.

    The -p setting makes directory only if necessary
    """
    for subfolder in ['source']:
        run('mkdir -p {0}/{1}'.format(site_folder, subfolder))


def _get_latest_source(source_folder, repo):
    """
    Clone repo.

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
    Updates the nginx sites-available, sites-enabled files.

    See the template used at project_dir/deploy/templates/nginxconf_template
    """
    nginxconf_template = "/deploy/templates/nginxconf_template"
    with open(project_dir + nginxconf_template, 'r') as f:
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
    Creates or updates the virtual environment.

    Postactivate script is updated based on template found at
    /.env/`deployment`.
    """
    if not exists(virtualenv_folder):
        run('mkvirtualenv ' + deployment)

    postactivate = source_folder + '/.env/' + deployment
    postvirtual = virtualenv_folder + '/bin/postactivate'
    run('ln -sf {0} {1}'.format(postactivate, postvirtual))
    workon = 'workon ' + deployment
    run(workon + ' && pip install -r ' + requirements)


def _update_settings(source_folder, deployment):
    """
    Adds a randomly generated `DJANGO_SECRET_KEY`.
    """
    postactivate = source_folder + '/.env/common'.format(deployment)
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&'
    key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
    key = "DJANGO_SECRET_KEY={0}".format(key)
    sed(postactivate, "DJANGO_SECRET_KEY=CHANGE_ME", key)


def _update_static_files(deployment, settings):
    """
    Runs `collectstatic`.
    """
    workon = 'workon ' + deployment
    collectstatic = workon + ' && python manage.py collectstatic --noinput'
    command = collectstatic + ' --settings=' + settings
    run(command)


def _update_database(deployment, settings):
    """
    Runs `migrate`.

    Please note that migrations should be commited and therefore makemigrations
    should not be part of the deployment script.
    """
    workon = 'workon ' + deployment
    migrate = workon + ' && python manage.py migrate --noinput'
    command = migrate + ' --settings=' + settings
    run(command)


def _restart_server(host, source_folder, deployment):
    """
    Restarts gunicorn processes.

    Uses 4 workers for the production server, while only 1 for staging.
    """
    if deployment == 'production':
        workers = '4'
    else:
        workers = '1'
    if exists(source_folder + "/gunicorn.pid"):
        run("kill `cat {0}/gunicorn.pid`".format(source_folder))
    venv = "workon {0} && ".format(deployment)
    startgunicorn = "gunicorn --bind unix:/tmp/HOST.socket "
    startgunicorn = startgunicorn.replace("HOST", host)
    startgunicorn += "config.wsgi:application --pid gunicorn.pid -w " + workers
    run(venv + startgunicorn)


# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    deploy()
