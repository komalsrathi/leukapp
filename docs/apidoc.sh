rm -rf _build
rm -rf leukapp
mkdir -p leukapp

sphinx-apidoc \
    -o leukapp\
    ../leukapp\
    ../leukapp/contrib\
    ../leukapp/*/tests\
    ../leukapp/*/migrations\

make html
