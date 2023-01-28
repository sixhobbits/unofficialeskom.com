#!/bin/zsh

source venv/bin/activate
mkdocs build

git add .
git commit -m "{$1}"
git push origin main

rsync -hvrPt site/* het:/var/www/unofficialeskom.com/


