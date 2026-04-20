# DynamoDB Skill

## Overview
Design DynamoDB tables with proper keys, GSIs, and capacity modes.

## Table Design

```hcl
resource "aws_dynamodb_table" "tasks" {
  name           = "tasks"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "userId"
  range_key      = "taskId"

  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "taskId"
    type = "S"
  }

  ttl {
    attribute_name = "expiresAt"
    enabled        = true
  }
}
```

## Key Types

| Key | Use Case |
|-----|----------|
| Partition Key (PK) | Single user queries |
| Sort Key (SK) | Time-based ordering |
| GSI | Alternative access patterns |
| LSI | Alternative sort order |

## Capacity Modes

| Mode | Use Case |
|------|----------|
| PAY_PER_REQUEST | Unpredictable traffic |
| PROVISIONED | Predictable, cost-effective |

## GSI Example

```hcl
global_secondary_index {
  name            = "status-index"
  hash_key        = "userId"
  range_key       = "status"
  projection_type = "ALL"
}
```

## Query Patterns

```javascript
// Get user's tasks
docClient.query({
  TableName: 'tasks',
  KeyConditionExpression: 'userId = :uid',
  ExpressionAttributeValues: {
    ':uid': userId
  }
})
```

## Best Practices

- Use on-demand for dev/test
- Enable TTL for auto-cleanup
- Project only needed attributes
- Use sparse indexes
