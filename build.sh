#!/bin/bash

cd "$(dirname "$0")"

source venv/bin/activate
cat LATEST_LOADSHEDDING_TWEET.txt > docs/latest/index.md

git add .
if [ "$1" != "" ] # or better, if [ -n "$1" ]
then
    git commit -m "$1"
else
    git commit -m update
fi
git push origin main

mkdocs build

cp -r site/* /var/www/unofficialeskom.com


