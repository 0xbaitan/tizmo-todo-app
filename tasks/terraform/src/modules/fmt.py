"""Terraform fmt module."""

from src.modules.config import TerraformCommand, get_terraform_dir, get_var_file


def build_fmt_cmd(env: str, check_only: bool = False) -> TerraformCommand:
    """
    Build terraform fmt command for the specified environment.

    Args:
        env: Environment name (development/production).
        check_only: If True, only check formatting without modifying files.

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    cmd = ["terraform", "-chdir=" + str(get_terraform_dir(env)), "fmt"]

    if check_only:
        cmd.append("-check")
        cmd.append("-diff")

    var_file = get_var_file(env)
    if var_file:
        cmd.extend(["-var-file", str(var_file)])

    return TerraformCommand(
        cmd=cmd,
        chdir=get_terraform_dir(env),
        var_file=var_file,
    )


def main(env: str, check_only: bool = False) -> TerraformCommand:
    """
    Main function for terraform fmt command.

    Args:
        env: Environment name (development/production).
        check_only: If True, only check formatting without modifying files.

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    return build_fmt_cmd(env, check_only)