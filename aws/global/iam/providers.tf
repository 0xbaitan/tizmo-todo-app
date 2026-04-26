provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
  alias      = "iam_admin"

  assume_role {
    role_arn = var.iam_admin_role_arn
  }
}
