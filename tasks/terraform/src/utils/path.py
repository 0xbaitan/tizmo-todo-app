"""Utility for resolving paths relative to project root directory."""

import os
from pathlib import Path


def get_root_dir() -> Path:
    """
    Get the project root directory from environment or default to parent of tasks/terraform.

    Returns:
        Path to the project root directory.
    """
    root = os.environ.get("ROOT_DIR")
    if root:
        return Path(root)
    # Default to parent of tasks/terraform
    return Path(__file__).parent.parent.parent.resolve()


def resolve_path(relative_path: str | Path) -> Path:
    """
    Resolve a path relative to the project root directory.

    Args:
        relative_path: Path relative to ROOT_DIR (e.g., "aws/environments/development").

    Returns:
        Absolute path resolved from ROOT_DIR.

    Examples:
        >>> resolve_path("aws/environments/development")
        PosixPath('/path/to/project/aws/environments/development')
        >>> resolve_path(".env.development.local")
        PosixPath('/path/to/project/.env.development.local')
    """
    root = get_root_dir()
    return root / relative_path