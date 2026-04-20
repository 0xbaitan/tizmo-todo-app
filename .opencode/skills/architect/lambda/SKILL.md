# Lambda Skill

## Overview
Design Lambda functions with proper VPC configuration, memory, timeout, and IAM roles.

## Function Configuration

```hcl
resource "aws_lambda_function" "example" {
  function_name    = "example-function"
  runtime          = "nodejs18.x"
  handler          = "index.handler"
  source_code_hash = filebase64sha256("lambda.zip")
  memory_size      = 256
  timeout          = 30

  vpc_config {
    subnet_ids         = aws_subnet.private[*].id
    security_group_ids = [aws_security_group.lambda.id]
  }
}
```

## Memory & Timeout

| Workload | Memory | Timeout |
|----------|--------|---------|
| Simple CRUD | 128-256 MB | 10-30s |
| API Handler | 256-512 MB | 30s |
| File Processing | 512-1024 MB | 60-300s |

## Cold Start Mitigation

- Use provisioned concurrency for critical APIs
- Set appropriate memory (more memory = faster CPU)
- Keep dependencies minimal
- Use arrow functions for faster init

## IAM Role

```hcl
data "aws_iam_policy_document" "lambda" {
  statement {
    effect = "Allow"
    actions = [
      "dynamodb:GetItem",
      "dynamodb:PutItem",
      "dynamodb:Query",
      "dynamodb:Scan",
    ]
    resources = ["arn:aws:dynamodb:*:*:table/tasks"]
  }
}
```

## VPC Considerations

- Lambda in VPC has cold starts (10-30s)
- Use VPC endpoints for S3/DynamoDB
- Place in private subnets only
- Security group with no inbound rules
