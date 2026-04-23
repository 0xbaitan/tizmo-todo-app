terraform {

  required_version = ">= 1.6.0"


  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92.0"
    }

  }
}

provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
}

module "lambda" {
  source = "../../modules/lambda"

  lambda_source_path = "/home/hexbaitan/Projects/tizmo-todo-app/apps/api/build/handler.js"
  lambda_zip_path    = "${path.module}/lambda.zip"

}

output "lambda_function_url" {
  value = module.lambda.lambda_function_url
}
