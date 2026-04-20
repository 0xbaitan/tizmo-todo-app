# S3 Skill

## Overview
Design S3 buckets for file storage with versioning, lifecycle policies, and access controls.

## Bucket Configuration

```hcl
resource "aws_s3_bucket" "assets" {
  bucket = "todo-assets-${var.environment}"
}

resource "aws_s3_bucket_versioning" "assets" {
  bucket = aws_s3_bucket.assets.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

## Bucket Policy

```hcl
data "aws_iam_policy_document" "s3_policy" {
  statement {
    effect = "Allow"
    principals {
      type = "*"
      identifiers = ["*"]
    }
    actions = ["s3:GetObject"]
    resources = ["${aws_s3_bucket.assets.arn}/*"]
  }
}
```

## Lifecycle Policy

```hcl
resource "aws_s3_bucket_lifecycle_policy" "assets" {
  bucket = aws_s3_bucket.assets.id
  rule {
    id     = "archive"
    status = "Enabled"
    transition {
      days          = 30
      storage_class = "GLACIER"
    }
    expiration {
      days = 365
    }
  }
}
```

## Use Cases

| Use Case | Configuration |
|---------|---------------|
| User uploads | Versioning enabled, private ACL |
| Public assets | CloudFront origin, public read |
| Backups | Lifecycle to Glacier |

## Security

- Block public access by default
- Use bucket policies for access
- Enable versioning for recovery
- Encrypt with SSE-KMS

## Cross-Region Replication

```hcl
resource "aws_s3_bucket_replication_configuration" "replica" {
  bucket = aws_s3_bucket.assets.id
  role   = aws_iam_role.replica.arn
  rule {
    id = "replicate"
    destination {
      bucket = aws_s3_bucket.replica.arn
    }
    status = "Enabled"
  }
}
```