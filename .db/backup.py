# -*- coding: utf-8 -*-

"""
Dumps a production database backup and current commit to **luna**.
"""

# python
from datetime import datetime

# third party
import environ
import paramiko
from scp import SCPClient
from subprocess import call
from time import sleep


def backuptoluna():
    """
    Dumps a production database backup and current commit to **luna**.

    For December the 3rd of 2015, the backup and commit are stored using this
    pattern::

        $LEUKDC_BACKUPDB_DIR/2015/12/3/db      # database backup
        $LEUKDC_BACKUPDB_DIR/2015/12/3/commit  # current commit

    This script relies heavily on the `scp`_ python package
    and the definition of environment variables at `.env/leukapp`.
    This script is called from `./backup.sh`. Please note that the virtualenv
    and the production database must be called `production`.

    .. important:
        `pg_dump`_ is a regular PostgreSQL client application. This means that
        you can perform this backup procedure from any remote host that has
        access to the database. But remember that `pg_dump`_ does not operate
        with special permissions. In particular, it must have read access to
        all tables that you want to back up, so in practice you almost always
        have to run it as a database superuser. To learn more see `pg_dump`_.

    .. _scp: https://github.com/jbardin/scp.py
    .. _pg_dump: http://www.postgresql.org/docs/9.1/static/backup-dump.html
    """

    # environment settings
    env = environ.Env()
    root = env('LEUKDC_BACKUPDB_DIR') + datetime.now().strftime("/%Y/%m/%d/")
    db, commit = "db", "commit"

    # ssh setting
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        env('LEUKDC_HOST'),
        username=env('LEUKDC_USER'),
        password=env('LEUKDC_PASSWORD'),
        key_filename=env('LEUKDC_SSHKEY'),
        )

    ssh.exec_command("mkdir -p " + root)
    sleep(1)  # Adds sleep to wait for ssh creation of directory

    # dump files
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(db, root)
        scp.put(commit, root)


# ROUTINE PROTECTION
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    backuptoluna()
