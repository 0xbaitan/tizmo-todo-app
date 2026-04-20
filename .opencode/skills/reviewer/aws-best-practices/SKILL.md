# AWS Best Practices Skill

## Overview
Review AWS implementations for serverless best practices.

## Lambda Best Practices

| Issue | Fix |
|-------|-----|
| 512MB+ memory | More memory = faster CPU |
| No cold start | Use provisioned concurrency |
| Verbose logging | Use structured JSON logging |
| Missing error handling | Wrap in try-catch |

## DynamoDB Best Practices

| Issue | Fix |
|-------|-----|
| Scan instead of Query | Use PK/SK queries |
| Missing GSI | Add GSI for access patterns |
| Provisioned underutilized | Switch to on-demand |
| No TTL | Enable for auto-cleanup |

## IAM Best Practices

| Issue | Fix |
|-------|-----|
| `*` in actions | Specific actions only |
| `*` in resources | Specific resource ARNs |
| No conditions | Add conditions |
| Inline policies | Use policy documents |

### Least Privilege Example

```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:GetItem",
    "dynamodb:PutItem"
  ],
  "Resource": "arn:aws:dynamodb:region:account:table/tasks",
  "Condition": {
    "ArnEquals": {
      "dynamodb:LeadingKeys": ["${cognito:sub}"]
    }
  }
}
```

## VPC Best Practices

- Private subnets for Lambda
- VPC endpoints for S3/DynamoDB
- NAT Gateway in public subnet
- Security groups with no inbound

## Cost Optimization

- Use on-demand for dev
- Delete unused resources
- Set CloudWatch retention
- Use Lambda layers