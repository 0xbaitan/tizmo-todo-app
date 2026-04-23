#!/usr/bin/env python3
"""
Terraform management script for development and production environments.

Provides interactive CLI to manage Terraform infrastructure with support for
both development and production environments.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from dotenv import load_dotenv

# Constants
ROOT_DIR = Path(__file__).parent.parent.resolve()
ENV_FILES = {
    "development": ".env.development.local",
    "production": ".env.production.local",
}
TERRAFORM_DIRS = {
    "development": ROOT_DIR / "aws" / "environments" / "development",
    "production": ROOT_DIR / "aws" / "environments" / "production",
}
REQUIRED_VARS = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]
TERRAFORM_COMMANDS = ["init", "plan", "apply", "destroy"]


def show_help():
    """Display help message and exit."""
    print("""Usage: terraform.py [-e ENV] [-c COMMAND] [-y] [-h]

Manage Terraform infrastructure for development or production environments.

Arguments:
  -e, --env ENV     Environment: development (d/dev) or production (p/prod)
                    If omitted, will prompt interactively.
  -c, --command CMD Terraform command to run (default: plan)
                    Can include additional flags (e.g., "apply -auto-approve")
  -y, --yes        Skip interactive confirmation for apply/destroy commands
  -h, --help       Show this help message and exit

Examples:
  terraform.py -e development -c init                         # Initialize dev
  terraform.py -e production -c "apply -auto-approve"         # Apply prod with auto-approve
  terraform.py -c "destroy -var-file=custom.tfvars" -e prod     # Destroy with custom vars
  terraform.py                                                # Interactive mode
""")
    sys.exit(0)


def parse_env_input(env_input: str) -> str | None:
    """Parse environment input and return full environment name."""
    env_input = env_input.lower().strip()

    if env_input in ("d", "dev", "development"):
        return "development"
    elif env_input in ("p", "prod", "production"):
        return "production"
    return None


def load_credentials(env: str) -> bool:
    """Load credentials from .env file for the specified environment."""
    env_file = ENV_FILES.get(env)
    if not env_file:
        return False

    env_file_path = ROOT_DIR / env_file
    if not env_file_path.exists():
        print(f"Error: {env_file} not found in {ROOT_DIR}")
        return False

    load_dotenv(dotenv_path=env_file_path)
    return True


def verify_env_vars() -> bool:
    """Verify required environment variables are set."""
    missing = [var for var in REQUIRED_VARS if not os.getenv(var)]
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        return False
    return True


def get_terraform_dir(env: str) -> Path:
    """Get the Terraform directory for the environment."""
    return TERRAFORM_DIRS.get(env, TERRAFORM_DIRS["development"])


def get_var_file(env: str) -> Path:
    """Get the tfvars file for the environment."""
    return get_terraform_dir(env) / "main.tfvars"


def run_terraform(env: str, command: str, auto_approve: bool = False) -> int:
    """Run terraform command in the specified environment directory."""
    tf_dir = get_terraform_dir(env)
    var_file = get_var_file(env)

    if not tf_dir.exists():
        print(f"Error: Terraform directory not found: {tf_dir}")
        return 1

    if not var_file.exists():
        print(f"Warning: Var file not found: {var_file}, skipping -var-file flag")

    # Build the terraform command
    tf_cmd = ["terraform", f"-chdir={tf_dir}"]

    # Parse the command - handle quoted arguments
    cmd_parts = command.strip().split()
    tf_cmd.extend(cmd_parts)

    # Add var-file if it exists
    if var_file.exists():
        tf_cmd.extend(["-var-file", str(var_file)])

    # Handle auto-approve
    base_cmd = cmd_parts[0] if cmd_parts else ""
    if auto_approve and base_cmd in ("apply", "destroy"):
        if "-auto-approve" not in cmd_parts:
            tf_cmd.append("-auto-approve")

    print(f"\nRunning: {' '.join(tf_cmd)}\n")

    try:
        result = subprocess.run(tf_cmd, check=False)
        return result.returncode
    except FileNotFoundError:
        print("Error: terraform command not found. Is Terraform installed?")
        return 1
    except Exception as e:
        print(f"Error running terraform: {e}")
        return 1


def interactive_mode() -> tuple[str, str, bool]:
    """Run in interactive mode, prompting for user input."""
    # Prompt for environment
    while True:
        env_input = input(
            "Do you want to manage for production or development environment "
            "[p,prod,production,d,dev,development]: "
        ).strip()

        env = parse_env_input(env_input)
        if env:
            break
        print("Invalid input. Please try again.")

    # Prompt for command
    while True:
        command = input(
            f"Terraform command [{', '.join(TERRAFORM_COMMANDS)}] (default: plan): "
        ).strip()
        if not command:
            command = "plan"
        break

    # Prompt for auto-approve if needed
    auto_approve = False
    base_cmd = command.split()[0]
    if base_cmd in ("apply", "destroy"):
        yes_input = input("Auto-approve? [y/N]: ").strip().lower()
        auto_approve = yes_input in ("y", "yes")

    return env, command, auto_approve


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        add_help=False,
        usage="terraform.py [-e ENV] [-c COMMAND] [-y] [-h]",
    )
    parser.add_argument("-e", "--env", type=str, default=None)
    parser.add_argument("-c", "--command", type=str, default=None)
    parser.add_argument("-y", "--yes", action="store_true", default=False)
    parser.add_argument("-h", "--help", action="store_true", default=False)

    args = parser.parse_args()

    if args.help:
        show_help()

    # Interactive or non-interactive
    if args.env is None:
        env, command, auto_approve = interactive_mode()
    else:
        env = parse_env_input(args.env)
        if not env:
            print("Error: Invalid environment. Use 'development'/'dev'/'d' or 'production'/'prod'/'p'")
            sys.exit(1)
        command = args.command if args.command else "plan"
        auto_approve = args.yes

    # Load credentials
    if not load_credentials(env):
        sys.exit(1)

    # Verify environment variables
    if not verify_env_vars():
        sys.exit(1)

    # Run terraform
    exit_code = run_terraform(env, command, auto_approve)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()