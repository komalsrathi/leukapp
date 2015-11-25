#!/bin/sh

# Creates a production database backup and dumps it to luna.
# This script is called from a cron job 5 mins before mid night every day
# the crob job settings are: 55 11 * * * /path/to/backup.sh
# It assumes that the virtualenv  and the database are called `production`.
# -----------------------------------------------------------------------------

# LOAD ENVIRONMENT
# -----------------------------------------------------------------------------
source /opt/rh/rh-python34/root/usr/bin/virtualenvwrapper.sh
workon production && cd .db

# BACKUP DATABSE
# -----------------------------------------------------------------------------
pg_dump production > db            # dump db backup
git log -n 1 --format=%H > commit  # save current commit
python backup.py                   # backup to luna
deactivate                         # deactivate virtual env
rm db commit                       # rm files
