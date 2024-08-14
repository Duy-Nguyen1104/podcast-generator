#!/bin/bash

# Echo a separator line for clarity
echo "========"

# Configure git with the provided GitHub actor and email
git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --add safe.directory /github/workspace

# Run the Python script
python3 /usr/bin/feed.py

# Add all changes, commit, and push to the main branch
git add . && git commit -m "Update Feed" 
if [ $? -eq 0 ]; then
    git push origin main
else
    echo "No changes to commit"
fi

# Echo a separator line for clarity
echo "========"
