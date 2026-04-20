#
# infrastructure/shared/providers.tf - Shared provider configuration
#

provider "aws" {
  region = var.region
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-2" # Default to London region, change as needed
}
