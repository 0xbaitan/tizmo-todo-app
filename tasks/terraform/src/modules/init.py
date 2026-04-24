"""Terraform init module."""

from src.modules.config import TerraformCommand, get_terraform_dir, get_var_file


def get_init_options() -> list[str]:
    """Get available options for terraform init command."""
    return ["-upgrade"]


def build_init_cmd(env: str) -> TerraformCommand:
    """
    Build terraform init command for the specified environment.

    Args:
        env: Environment name (development/production).

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    cmd = ["terraform", "-chdir=" + str(get_terraform_dir(env)), "init"]

    var_file = get_var_file(env)
    if var_file:
        cmd.extend(["-var-file", str(var_file)])

    return TerraformCommand(
        cmd=cmd,
        chdir=get_terraform_dir(env),
        var_file=var_file,
    )


def main(env: str) -> TerraformCommand:
    """
    Main function for terraform init command.

    Args:
        env: Environment name (development/production).

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    return build_init_cmd(env)