# CI/CD Skill

## Overview
Design GitHub Actions workflows for testing, linting, and deployment.

## Workflow Structure

```
.github/workflows/
├── test.yml     # Lint + Test
├── deploy.yml   # Deploy to AWS
└── release.yml # Electron build
```

## Test Workflow

```yaml
name: Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run lint
      - run: npm test
```

## Deploy Workflow

```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: '1.6'
      - run: terraform fmt -check
      - run: terraform plan
      - run: terraform apply -auto-approve
```

## Electron Release

```yaml
name: Release
on:
  release:
    types: [created]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build
      - uses: electron-builder/action@0.4
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

## Best Practices

- Run lint before tests
- Use `npm ci` not `npm install`
- Cache dependencies
- Use `[skip ci]` to skip builds
- Require checks before merge

## Secrets Management

- Use GitHub secrets for AWS keys
- Never commit secrets
- Use IAM roles with short-lived creds