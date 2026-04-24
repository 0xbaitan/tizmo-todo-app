"""Main orchestrator for Terraform CLI."""

import os
import subprocess
import sys
from pathlib import Path

from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.filters import is_done
from prompt_toolkit.formatted_text.html import HTML
from prompt_toolkit.shortcuts import choice, confirm, yes_no_dialog
from prompt_toolkit.styles import Style

from src.modules import config
from src.modules import destroy as destroy_module
from src.modules import fmt as fmt_module
from src.modules import init as init_module
from src.modules import plan as plan_module
from src.utils import autoprefix_env_vars, load_env

style = Style.from_dict(
    {
        "frame.border": "#884444",
        "selected-option": "bold bg:#884444 fg:#000000",
    }
)


def get_root_dir() -> Path:
    """Get the project root directory from environment or current directory."""
    root = os.environ.get("ROOT_DIR")
    if root:
        return Path(root)
    return Path(__file__).parent.resolve()


def load_environment(env: str) -> bool:
    """
    Load environment variables for the specified environment.

    Args:
        env: Environment name (development/production).

    Returns:
        True if successful, False otherwise.
    """
    root_dir = get_root_dir()
    env_file = config.get_env_file(env)
    env_file_path = root_dir / env_file

    if not env_file_path.exists():
        print(f"Error: {env_file} not found in {root_dir}")
        return False

    try:
        env_vars = load_env.load_env(env_file_path)
        # Apply environment variables to os.environ
        for key, value in env_vars.items():
            os.environ[key] = value

        # Transform credentials for Terraform
        tf_vars = autoprefix_env_vars.autoprefix_env_vars(env_vars)
        for key, value in tf_vars.items():
            os.environ[key] = value

        return True
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False


def verify_environment() -> bool:
    """Verify required environment variables are set."""
    required = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]
    missing = [var for var in required if var not in os.environ]
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        return False
    return True


def run_terraform_command(cmd_config: config.TerraformCommand) -> int:
    """
    Run a terraform command.

    Args:
        cmd_config: Dictionary with cmd, chdir, and var_file.

    Returns:
        Exit code from terraform command.
    """
    root_dir = get_root_dir()
    tf_dir = root_dir / cmd_config["chdir"]

    if not tf_dir.exists():
        print(f"Error: Terraform directory not found: {tf_dir}")
        return 1

    cmd = cmd_config["cmd"]

    print(f"\nRunning: {' '.join(cmd)}\n")

    try:
        result = subprocess.run(
            cmd,
            cwd=root_dir,
            env=os.environ.copy(),
        )
        return result.returncode
    except FileNotFoundError:
        print("Error: terraform command not found. Is Terraform installed?")
        return 1
    except Exception as e:
        print(f"Error running terraform: {e}")
        return 1


def select_environment() -> str:
    """Prompt user to select an environment."""

    result = choice(
        message="Select environment:",
        options=[
            ("development", "development"),
            ("production", "production"),
        ],
        bottom_toolbar=HTML(
            "Press <b>[Up]</b>/<b>[Down]</b> to select, <b>[Enter]</b> to accept."
        ),
        style=style,
        show_frame=(not is_done()),
    )
    return result


def select_command() -> str:
    """Prompt user to select a terraform command."""
    result = choice(
        message="Select terraform command:",
        options=[
            ("init", "init"),
            ("plan", "plan"),
            ("fmt", "fmt"),
            ("destroy", "destroy"),
        ],
        style=style,
        show_frame=(not is_done()),
    )

    return result


def run_interactive() -> None:
    """Run the CLI in interactive mode."""
    # Select environment
    env = select_environment()
    if not env:
        print("No environment selected. Exiting.")
        sys.exit(0)

    # Load environment variables
    if not load_environment(env):
        sys.exit(1)

    # Verify required variables
    if not verify_environment():
        sys.exit(1)

    # Select command
    cmd = select_command()
    if not cmd:
        print("No command selected. Exiting.")
        sys.exit(0)

    # Execute command
    cmd_config: config.TerraformCommand = plan_module.main(env)  # Default to plan

    if cmd == "init":
        cmd_config = init_module.main(env)
    elif cmd == "plan":
        cmd_config = plan_module.main(env)
    elif cmd == "fmt":
        cmd_config = fmt_module.main(env)
    elif cmd == "destroy":
        # Confirm before destroy
        should_proceed = yes_no_dialog(
            title="Confirm Destroy",
            text="Are you sure you want to destroy the infrastructure? This action cannot be undone.",
            yes_text="Yes, destroy",
            no_text="No, cancel",
        ).run()
        if should_proceed:
            cmd_config = destroy_module.main(env)
        else:
            print("Destroy cancelled.")
            sys.exit(0)

    exit_code = run_terraform_command(cmd_config)
    sys.exit(exit_code)


def main() -> None:
    """Main entry point."""
    run_interactive()


if __name__ == "__main__":
    main()
