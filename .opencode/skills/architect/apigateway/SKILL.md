# API Gateway Skill

## Overview
Design REST APIs with API Gateway, Lambda integration, and Cognito authorizer.

## Basic API Structure

```hcl
resource "aws_api_gateway_rest_api" "todo" {
  name = "todo-api"
}

resource "aws_api_gateway_resource" "tasks" {
  rest_api_id = aws_api_gateway_rest_api.todo.id
  parent_id   = aws_api_gateway_rest_api.todo.root_resource_id
  path_part   = "tasks"
}

resource "aws_api_gateway_method" "get_tasks" {
  rest_api_id   = aws_api_gateway_rest_api.todo.id
  resource_id   = aws_api_gateway_resource.tasks.id
  http_method   = "GET"
  authorization = "COGNITO_USER_POOLS"
  authorizer_id = aws_api_gateway_authorizer.cognito.id
}
```

## REST Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /tasks | List tasks |
| POST | /tasks | Create task |
| GET | /tasks/{id} | Get task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

## Authentication

```hcl
resource "aws_api_gateway_authorizer" "cognito" {
  rest_api_id   = aws_api_gateway_rest_api.todo.id
  name          = "cognito-authorizer"
  type          = "COGNITO_USER_POOLS"
  provider_arns = [aws_cognito_user_pool.pool.arn]
}
```

## CORS Configuration

```hcl
resource "aws_api_gateway_method" "cors" {
  rest_api_id   = aws_api_gateway_rest_api.todo.id
  resource_id   = aws_api_gateway_resource.tasks.id
  http_method   = "OPTIONS"
  authorization = "NONE"
}
```

## Rate Limiting

- Enable throttling: `burst_limit` and `rate_limit`
- Use API Gateway usage plans for tiered access
- Default: 10,000 requests/second

## Lambda Integration

```hcl
resource "aws_api_gateway_integration" "lambda" {
  rest_api_id = aws_api_gateway_rest_api.todo.id
  resource_id = aws_api_gateway_resource.tasks.id
  type        = "AWS_PROXY"
  uri         = aws_lambda_function.handler.invoke_arn
}
