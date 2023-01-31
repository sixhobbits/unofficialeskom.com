#!/bin/bash

# set working dir
cd "$(dirname "$0")"

# fetch latest handbook
# git reset --hard
rm -rf site
git pull

# build static site
source ./venv/bin/activate
mkdocs build

# scp static files to production
cp -r site/* /var/www/unofficialeskom.com
