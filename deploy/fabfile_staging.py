"""
fab deploy:host=medinaj@plvleukweb1.mskcc.org -f fabfile_staging.py
"""

# python
import random

# third party
from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run

REPO_URL = 'git@github.com:leukgen/leukapp.git'


def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ['source']:
        run('mkdir -p %s/%s' % (site_folder, subfolder))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))


def _update_settings(source_folder, site_name):
    """ not needed because we have different settings files """
    pass


def _update_virtualenv(source_folder):
    # check if virtualenv exists
    virtualenv_folder = '/home/medinaj/.virtualenvs/staging'
    if not exists(virtualenv_folder):
        run('mkvirtualenv staging')

    # Install requirements:
    requirements = source_folder + '/requirements/production.txt'
    run('%s/bin/pip install -r %s' % (virtualenv_folder, requirements))


def _update_static_files(source_folder):
    python = '/home/medinaj/.virtualenvs/staging/bin/python'
    command = 'workon staging && cd {0} && {1} {2} {3}'
    collectstatic = 'manage.py collectstatic --noinput'
    config = '--settings=config.settings.staging'
    run(command.format(source_folder, python, collectstatic, config))
    pass


def _update_database(source_folder):
    # migrate
    python = '/home/medinaj/.virtualenvs/staging/bin/python'
    command = 'workon staging && cd {0} && {1} {2} {3}'
    migrate = 'manage.py migrate --noinput'
    config = '--settings=config.settings.staging'
    run(command.format(source_folder, python, migrate, config))
