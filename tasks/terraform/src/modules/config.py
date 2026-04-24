"""Constants and configuration for terraform modules."""

from pathlib import Path
from typing import TypedDict

from src.utils.path import get_root_dir, resolve_path


class TerraformCommand(TypedDict):
    """Return type for terraform command builders."""

    cmd: list[str]
    chdir: Path
    var_file: Path | None


# Environment directories relative to project root
TERRAFORM_DIRS: dict[str, Path] = {
    "development": resolve_path("aws/environments/development"),
    "production": resolve_path("aws/environments/production"),
}

# Environment file mapping
ENV_FILES: dict[str, str] = {
    "development": ".env.development.local",
    "production": ".env.production.local",
}

PLAN_DIRS: dict[str, Path] = {
    "development": resolve_path("aws/plans/development"),
    "production": resolve_path("aws/plans/production"),
}

# Available terraform commands
TERRAFORM_COMMANDS = ["init", "plan", "apply", "fmt", "destroy"]


def get_root() -> Path:
    """Get the project root directory."""
    return get_root_dir()


def get_terraform_dir(env: str) -> Path:
    """Get the terraform directory for the environment."""
    return TERRAFORM_DIRS.get(env, TERRAFORM_DIRS["development"])


def get_env_file(env: str) -> Path:
    """Get the env file path for the environment."""
    return resolve_path(ENV_FILES.get(env, ENV_FILES["development"]))


def get_var_file(env: str) -> Path | None:
    """Get the var file path for the environment."""
    var_file = get_terraform_dir(env) / "main.tfvars"
    return var_file if var_file.exists() else None


def get_plan_dir(env: str) -> Path:
    """Get the plan directory for the environment."""
    return PLAN_DIRS.get(env, PLAN_DIRS["development"])