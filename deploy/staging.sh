fab \
    deploy:host=medinaj@plvleukweb1.mskcc.org \
    -f $PROJECT_DIR/deploy/fabfile.py \
    --set=DEPLOYMENT=staging,REPO_URL=git@github.com:leukgen/leukapp.git,REQUIREMENTS=production.txt,DJ_SETTINGS=config.settings.production,PROJECT_DIR=$PROJECT_DIR\
