
variable "aws_region" {
  type        = string
  description = "The AWS region for the development environment"
  default     = "eu-west-2" # Default to London region, change as needed
}

variable "aws_account_id" {
  type        = string
  description = "The AWS account ID for the development environment"
}

variable "aws_access_key_id" {
  type        = string
  description = "The AWS access key ID for the development environment"
  sensitive   = true
}

variable "aws_secret_access_key" {
  type        = string
  description = "The AWS secret access key for the development environment"
  sensitive   = true
}

variable "localstack_host" {
  type        = string
  description = "The hostname for LocalStack in the development environment"
}


