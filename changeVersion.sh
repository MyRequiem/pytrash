#! /bin/sh

if [ "x$1" == "x" ]; then
    echo "Usage: ./$(basename "$0") version"
    exit 1
fi

VERSION="$1"
INFILE="
    INSTALL
    README.md
    slackbuild/pytrash.info
"

for FILE in ${INFILE}; do
    sed "s/[0-9]\\.[0-9]\\.[0-9]/${VERSION}/g" "${FILE}" > "${FILE}_"
    rm -f "${FILE}"
    mv "${FILE}_" "${FILE}"
done
