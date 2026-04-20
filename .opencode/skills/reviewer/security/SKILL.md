# Security Skill

## Overview
Review code for security vulnerabilities and ensure secure coding practices.

## Critical Issues (Blockers)

| Issue | Description | Fix |
|-------|------------|-----|
| SQL Injection | Raw SQL with user input | Use parameterized queries |
| XSS | Unescaped user content | Escape/-sanitize output |
| Command Injection | exec/eval with user input | Avoid, use safe APIs |
| Secrets in Code | API keys, passwords hardcoded | Use env variables |
| Auth Bypass | Missing auth checks | Verify on every request |

## Input Validation

```typescript
// Always validate input
function createTask(data: unknown) {
  if (!data || typeof data !== 'object') {
    throw new Error('Invalid input')
  }
  const task = data as TaskInput
  if (!task.title || task.title.length === 0) {
    throw new Error('Title required')
  }
  if (task.title.length > 200) {
    throw new Error('Title too long')
  }
}
```

## Authentication

```typescript
// Verify on every protected route
export async function GET(request: Request) {
  const user = await authenticate(request)
  if (!user) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }
  // Proceed with user.id
}
```

## Secrets

- NEVER commit secrets to git
- Use environment variables
- AWS SSM for production secrets
- .gitignore for .env files

## Common Patterns

| Pattern | Issue | Secure Alternative |
|---------|-------|---------------|
| `eval()` | Command injection | Don't use eval |
| `innerHTML` | XSS | textContent or escape |
| `fs.readFile(path)` | Path traversal | Validate path |
| SQL string concat | SQL injection | Parameterized query |