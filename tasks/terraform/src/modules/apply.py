"""Terraform apply module."""

from pathlib import Path

from src.modules.config import TerraformCommand, get_terraform_dir, get_var_file


def get_apply_options() -> list[str]:
    """Get available options for terraform apply command."""
    return ["-auto-approve", "-var-file"]


def build_apply_cmd(env: str, plan_file_path: Path | None = None) -> TerraformCommand:
    """
    Build terraform apply command for the specified environment.

    Args:
        env: Environment name (development/production).
        plan_file_path: Optional path to the plan file to apply.

    Returns:
        TerraformCommand with command, chdir, and var_file.
    """
    cmd = ["terraform", "-chdir=" + str(get_terraform_dir(env)), "apply"]

    var_file = get_var_file(env)
    if var_file:
        cmd.extend(["-var-file", str(var_file)])

    if plan_file_path:
        cmd.append(plan_file_path.as_posix())

    return TerraformCommand(
        cmd=cmd,
        chdir=get_terraform_dir(env),
        var_file=var_file,
    )


def main(env: str, plan_file_path: Path | None = None) -> TerraformCommand:
    """
    Main function for terraform apply command.

    Args:
        env: Environment name (development/production).
        plan_file_path: Optional path to the plan file to apply.

    Returns:
        TerraformCommand with command, chdir, and var_file.
    """
    return build_apply_cmd(env, plan_file_path)