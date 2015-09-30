rm -rf _build
rm -rf leukgen
mkdir -p leukgen

sphinx-apidoc \
    -o leukgen\
    ../leukgen\
    ../leukgen/contrib\
    ../leukgen/*/tests\
    ../leukgen/*/migrations\

make html
