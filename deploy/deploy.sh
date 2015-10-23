fab \
    deploy:host=medinaj@plvleukweb1.mskcc.org \
    -f fabfile.py \
    --set=VIRTUALENV=staging,REPO_URL=git@github.com:leukgen/leukapp.git,REQUIREMENTS=production.txt,DJ_SETTINGS=config.settings.staging\
