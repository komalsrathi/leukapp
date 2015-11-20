rm -rf build
rm -rf source/leukapp
mkdir -p source/leukapp

sphinx-apidoc \
    -o source/leukapp \
    $PROJECT_DIR/leukapp \
    $PROJECT_DIR/leukapp/contrib \
    $PROJECT_DIR/leukapp/apps/lists \
    $PROJECT_DIR/leukapp/apps/*/tests \
    $PROJECT_DIR/leukapp/apps/*/migrations \

make html
