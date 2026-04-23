#!/usr/bin/env python3

"""
Load AWS credentials from .env files, prefix them, and export them as environment variables for Terraform to use.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

CREDENTIALS = ['ACCESS_KEY_ID', 'SECRET_ACCESS_KEY']


def load_env_file(env_file_path):
    if not env_file_path.exists():
        print(f"Error: {env_file_path} does not exist.")
        sys.exit(1)
    load_dotenv(dotenv_path=env_file_path)


def print_prefixed_env_vars():
    for key, value in os.environ.items():
        if key in CREDENTIALS:
            prefixed_key = f"TF_VAR_{key.lower()}"
            print(f"export {prefixed_key}={value}")


if __name__ == "__main__":
    env_file = '.env.development.local' if os.getenv(
        'ENV') == 'dev' else '.env.production.local'
    env_file_path = os.path.join(os.getenv('ROOT_DIR', '.'), env_file)
    load_env_file(Path(env_file_path))
    print_prefixed_env_vars()
