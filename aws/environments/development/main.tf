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
  region                      = var.aws_region
  access_key                  = var.aws_access_key_id
  secret_key                  = var.aws_secret_access_key
  s3_use_path_style           = true
  skip_requesting_account_id  = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true # Skip checking for EC2 metadata service, since we're using localstack
  endpoints {
    iam            = "http://iam.${var.localstack_host}:4566"
    apigateway     = "http://apigateway.${var.localstack_host}:4566"
    s3             = "http://s3.${var.localstack_host}:4566"
    dynamodb       = "http://dynamodb.${var.localstack_host}:4566"
    cloudformation = "http://cloudformation.${var.localstack_host}:4566"
    cloudwatch     = "http://cloudwatch.${var.localstack_host}:4566"
    cloudwatchlogs = "http://cloudwatchlogs.${var.localstack_host}:4566"
    ec2            = "http://ec2.${var.localstack_host}:4566"
    lambda         = "http://lambda.${var.localstack_host}:4566"
  }

}

module "lambda" {
  source = "../../modules/lambda"

  lambda_source_path = "/home/hexbaitan/Projects/tizmo-todo-app/apps/api/build/handler.js"
  lambda_zip_path    = "${path.module}/lambda.zip"

}

output "lambda_function_url" {
  value = module.lambda.lambda_function_url
}
