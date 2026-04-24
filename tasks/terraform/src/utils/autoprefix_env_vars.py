"""Utility for autoprefixing environment variables for Terraform."""

import os


def autoprefix_env_vars(env_dict: dict[str, str]) -> dict[str, str]:
    """
    Transform AWS credentials to Terraform variable format.

    Converts AWS_ACCESS_KEY_ID -> TF_VAR_aws_access_key_id
    Converts AWS_SECRET_ACCESS_KEY -> TF_VAR_aws_secret_access_key

    Args:
        env_dict: Dictionary of environment variables.

    Returns:
        Dictionary with TF_VAR prefixed variables.
    """
    result = {}

    for key, value in env_dict.items():
        if key == "AWS_ACCESS_KEY_ID":
            result["TF_VAR_aws_access_key_id"] = value
        elif key == "AWS_SECRET_ACCESS_KEY":
            result["TF_VAR_aws_secret_access_key"] = value

    return result


def get_required_env_vars(env_dict: dict[str, str]) -> list[str]:
    """
    Get list of missing required environment variables.

    Args:
        env_dict: Dictionary of environment variables.

    Returns:
        List of missing variable names.
    """
    required = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]
    return [var for var in required if var not in env_dict]