#!/bin/bash
set -e

echo "Installing Git hooks..."
cp .githooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
echo "Pre-commit hook installed!"
