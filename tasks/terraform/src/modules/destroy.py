"""Terraform destroy module."""

from src.modules.config import TerraformCommand, get_terraform_dir, get_var_file


def get_destroy_options() -> list[str]:
    """Get available options for terraform destroy command."""
    return ["-auto-approve", "-var-file"]


def build_destroy_cmd(env: str) -> TerraformCommand:
    """
    Build terraform destroy command for the specified environment.

    Args:
        env: Environment name (development/production).

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    cmd = ["terraform", "-chdir=" + str(get_terraform_dir(env)), "destroy"]

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
    Main function for terraform destroy command.

    Args:
        env: Environment name (development/production).

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    return build_destroy_cmd(env)