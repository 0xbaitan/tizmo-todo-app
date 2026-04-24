"""Constants and configuration for terraform modules."""

import os
from pathlib import Path
from typing import TypedDict


class TerraformCommand(TypedDict):
    """Return type for terraform command builders."""

    cmd: list[str]
    chdir: Path
    var_file: Path | None


# Environment directories relative to project root
TERRAFORM_DIRS: dict[str, Path] = {
    "development": Path(f"{os.getenv('ROOT_DIR')}/aws/environments/development"),
    "production": Path(f"{os.getenv('ROOT_DIR')}/aws/environments/production"),
}

# Environment file mapping
ENV_FILES: dict[str, str] = {
    "development": ".env.development.local",
    "production": ".env.production.local",
}

# Available terraform commands
TERRAFORM_COMMANDS = ["init", "plan", "apply", "fmt", "destroy"]


def get_terraform_dir(env: str) -> Path:
    """Get the terraform directory for the environment."""
    return TERRAFORM_DIRS.get(env, TERRAFORM_DIRS["development"])


def get_env_file(env: str) -> str:
    """Get the env file name for the environment."""
    return ENV_FILES.get(env, ".env.development.local")


def get_var_file(env: str) -> Path | None:
    """Get the var file path for the environment."""
    var_file = get_terraform_dir(env) / "main.tfvars"
    return var_file if var_file.exists() else None
