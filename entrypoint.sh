#!bin/bash

echo "========"

git config --global user.name "${GITHUB_ACTOR}
git config --global user.name "${INPUT_EMAIL}
git config --add safe.directory /github/workspace

python3 /usr/bin/feed.py

git add . && git commit -m "Update Feed" 
git push --set-upstream origin main

echo "========"
