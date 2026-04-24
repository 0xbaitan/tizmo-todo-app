"""Terraform plan module."""

from pathlib import Path

from src.modules.config import TerraformCommand, get_terraform_dir, get_var_file


def get_plan_options() -> list[str]:
    """Get available options for terraform plan command."""
    return ["-out", "-var-file"]


def build_plan_cmd(env: str, out_file: Path | None = None) -> TerraformCommand:
    """
    Build terraform plan command for the specified environment.

    Args:
        env: Environment name (development/production).
        out_file: Optional output file path for the plan.

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    cmd = ["terraform", "-chdir=" + str(get_terraform_dir(env)), "plan"]

    var_file = get_var_file(env)
    if var_file:
        cmd.extend(["-var-file", str(var_file)])

    if out_file:
        cmd.extend(["-out", out_file.as_posix()])

    return TerraformCommand(
        cmd=cmd,
        chdir=get_terraform_dir(env),
        var_file=var_file,
    )


def main(env: str, out_file: Path | None = None) -> TerraformCommand:
    """
    Main function for terraform plan command.

    Args:
        env: Environment name (development/production).
        out_file: Optional output file path for the plan.

    Returns:
        Dictionary with command, chdir, and var_file.
    """
    return build_plan_cmd(env, out_file)
