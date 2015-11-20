sphinx-apidoc \
    -f `remove files` \
    -e `put submodules in separate directories` \
    -o source/leukapp `output directory` \
    $PROJECT_DIR/leukapp `source directory` \
    $PROJECT_DIR/leukapp/contrib `exclude path` \
    $PROJECT_DIR/leukapp/apps/lists `exclude path` \
    $PROJECT_DIR/leukapp/apps/*/tests `exclude path` \
    $PROJECT_DIR/leukapp/apps/*/migrations `exclude path` \

make html
