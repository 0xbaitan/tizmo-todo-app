
variable "aws_region" {
  type        = string
  description = "The AWS region"
  default     = "eu-west-2" # Default to London region, change as needed
}

variable "aws_account_id" {
  type        = string
  description = "The AWS account ID"
}

variable "aws_access_key_id" {
  type        = string
  description = "The AWS access key ID"
  sensitive   = true
}

variable "aws_secret_access_key" {
  type        = string
  description = "The AWS secret access key"
  sensitive   = true
}

variable "iam_admin_role_arn" {
  type        = string
  description = "The ARN of the IAM role with administrative privileges"
}
