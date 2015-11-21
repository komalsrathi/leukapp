# for the -M flag, see:
# https://bitbucket.org/birkenfeld/sphinx/pull-requests/236/1456-apidoc-add-a-m-option-to-put-module/diff

sphinx-apidoc \
    -f `# remove files` \
    -M `# put module first` \
    -e `# put submodules in separate directories` \
    -d 2 `# Maximum depth generated in table of contents file.`\
    -o source/leukapp `# output directory` \
    $PROJECT_DIR/leukapp `# source directory` \
    $PROJECT_DIR/leukapp/contrib `# exclude path` \
    $PROJECT_DIR/leukapp/apps/lists `# exclude path` \
    $PROJECT_DIR/leukapp/apps/*/tests `# exclude path` \
    $PROJECT_DIR/leukapp/apps/*/migrations `# exclude path` \

make html
