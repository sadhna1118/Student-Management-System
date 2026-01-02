#!/usr/bin/env bash
# Build script for deployment

set -o errexit

# Install dependencies
pip install -r requirements.txt

# Initialize database
python scripts/init_db.py

echo "Build completed successfully!"