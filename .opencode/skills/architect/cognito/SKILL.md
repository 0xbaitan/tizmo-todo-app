# Cognito Skill

## Overview
Design Cognito User Pool for authentication with MFA, attributes, and secure defaults.

## User Pool Configuration

```hcl
resource "aws_cognito_user_pool" "pool" {
  name = "todo-user-pool"

  password_policy {
    minimum_length    = 8
    require_lowercase = true
    require_numbers   = true
    require_symbols  = true
    require_uppercase = false
  }

  username_attributes = ["email"]
  alias_attributes   = ["email"]

  auto_verified_attributes = ["email"]

  schema {
    attribute_data_type = "String"
    name            = "email"
    required        = true
  }
}
```

## App Client

```hcl
resource "aws_cognito_user_pool_client" "client" {
  name                = "todo-app-client"
  user_pool_id        = aws_cognito_user_pool.pool.id
  generate_secret     = false
  allowed_oauth_flows = ["code"]
  allowed_oauth_scopes = ["email", "openid"]
  callback_urls       = ["http://localhost:3000/callback"]
  logout_urls        = ["http://localhost:3000/logout"]
}
```

## MFA Settings

| Setting | Security |
|---------|----------|
| OFF | No MFA |
| OPTIONAL | User choice |
| ON (Required) | Highest security |

## Supported Login

- Email/password
- OAuth 2.0 (Google, etc.)
- SAML federation

## Security

- Enable MFA for production
- Use alias (email) not username
- Configure app client secrets
- Set token expiration