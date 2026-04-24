from pathlib import Path

from src.modules.config import TerraformCommand, get_terraform_dir


def build_show_cmd(
    env: str, plan_file_path: Path, show_json: bool = False
) -> TerraformCommand:
    """
    Build terraform show command for the specified environment.

    Args:
        env: Environment name (development/production).
        plan_file: Optional path to the plan file to show.
    """
    cmd = ["terraform", "-chdir=" + str(get_terraform_dir(env)), "show"]
    if show_json:
        cmd.append("-json")

    if plan_file_path:
        cmd.append(plan_file_path.as_posix())

    return TerraformCommand(cmd=cmd, chdir=get_terraform_dir(env), var_file=None)
