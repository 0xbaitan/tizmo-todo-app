# Developer Terraform Skill

## Overview
Implement Terraform configurations following architect's designs.

## File Structure

```
infrastructure/
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── lambda/
├── core/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── localstack/
```

## Module Template

```hcl
# main.tf
resource "aws_dynamodb_table" "this" {
  name           = var.name
  billing_mode   = var.billing_mode
  hash_key      = var.hash_key

  dynamic "attribute" {
    for_each = var.attributes
    content {
      name = attribute.value.name
      type = attribute.value.type
    }
  }
}
```

```hcl
# variables.tf
variable "name" {
  description = "Table name"
  type        = string
}

variable "hash_key" {
  description = "Partition key"
  type        = string
}
```

## Commands

```bash
cd infrastructure/core
terraform init
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
```

## Best Practices

- Use modules for reusability
- Define minimum required variables
- Export useful outputs
- Always run `terraform fmt`
- Use `.gitignore` for state files