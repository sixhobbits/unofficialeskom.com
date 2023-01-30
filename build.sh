#!/bin/bash

source venv/bin/activate
mkdocs build

git add .
if [ "$1" != "" ] # or better, if [ -n "$1" ]
then
    git commit -m "$1"
else
    git commit -m update
fi
git push origin main

cat LATEST_LOADSHEDDING_TWEET.txt > docs/latest/index.md

cp -r site/* /var/www/unofficialeskom.com


