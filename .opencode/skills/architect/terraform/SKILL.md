# Terraform Skill

## Overview
Design and review Terraform infrastructure as code for AWS resources.

## Key Principles

1. **Module Design**: Create reusable, composable modules
2. **State Management**: Use S3 backend with DynamoDB locking
3. **Variables**: Define clear inputs with validation
4. **Outputs**: Expose values needed by other modules
5. **Formatting**: Run `terraform fmt` on all files

## Core Commands

```bash
terraform init          # Initialize backend
terraform validate      # Validate syntax
terraform plan         # Preview changes
terraform apply        # Apply changes
terraform destroy      # Tear down
terraform fmt          # Format code
```

## AWS Resources

| Resource | Purpose |
|----------|---------|
| aws_vpc | Virtual Private Cloud |
| aws_subnet | Subnets (public/private) |
| aws_security_group | Firewall rules |
| aws_iam_role | Lambda execution role |
| aws_lambda_function | Lambda function |
| aws_dynamodb_table | DynamoDB table |
| aws_s3_bucket | S3 storage |
| aws_apigatewayv2_api | API Gateway |

## Best Practices

- Use `terraform { required_version = ">= 1.0" }`
- Pin provider versions
- Enable versioning on state bucket
- Use workspaces for environments
- Tag all resources

## Security

- Never commit `.tfstate` files
- Use `.gitignore` for state files
- Enable S3 bucket versioning
- Use IAM roles, not access keys
