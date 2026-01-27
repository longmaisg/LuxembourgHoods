#!/bin/bash
# Quick commit and push script
# Usage: ./commit.sh "commit message"

set -e

if [ -z "$1" ]; then
    echo "Usage: ./commit.sh \"commit message\""
    exit 1
fi

MSG="$1"
HASH_SHORT=""

# Add all changes
git add -A

# Commit
git commit -m "$MSG

Co-Authored-By: Claude <noreply@anthropic.com>"

# Get short hash
HASH_SHORT=$(git rev-parse --short HEAD)

# Push
git push origin main 2>/dev/null || git push origin master 2>/dev/null || git push

# Log to CHANGELOG
echo "- [$HASH_SHORT] $(date '+%Y-%m-%d %H:%M') $MSG" >> CHANGELOG.md

echo "✓ Committed and pushed: $HASH_SHORT"
