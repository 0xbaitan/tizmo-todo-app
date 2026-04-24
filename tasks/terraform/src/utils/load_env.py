"""Utility for loading environment variables from .env files."""

from pathlib import Path
from typing import Any

from dotenv import dotenv_values


def load_env(env_file_path: Path) -> dict[str, str]:
    """
    Load environment variables from .env file.

    Args:
        env_file_path: Path to the .env file.

    Returns:
        Dictionary of environment variables.

    Raises:
        FileNotFoundError: If the env file does not exist.
    """
    if not env_file_path.exists():
        raise FileNotFoundError(f"Environment file not found: {env_file_path}")

    env_vars: dict[str, Any] = dotenv_values(env_file_path)
    # Convert Values to strings, filtering out None values
    return {k: str(v) for k, v in env_vars.items() if v is not None}