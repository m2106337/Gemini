#!/bin/sh
set -euo pipefail

# Install requirements from the mounted workspace if present
if [ -f /github/workspace/requirements.txt ]; then
  python -m pip install --upgrade pip
  pip install -r /github/workspace/requirements.txt
fi

# Run the gemini CLI from the checked out repository
exec python /github/workspace/gemini.py "$@"
