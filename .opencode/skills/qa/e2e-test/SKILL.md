# E2E Test Skill

## Overview
Design and write end-to-end tests for full user workflows in the desktop app.

## Test Framework

Use Playwright for Electron E2E testing.

## Test Structure

```typescript
import { test, expect } from '@playwright/test'

test('create and complete task', async ({ app }) => {
  // Launch app
  await app.start()

  // Login
  await app.click('[data-testid="login"]')
  await app.fill('[data-testid="email"]', 'test@example.com')
  await app.fill('[data-testid="password"]', 'password')
  await app.click('[data-testid="submit"]')

  // Create task
  await app.click('[data-testid="add-task"]')
  await app.fill('[data-testid="title"]', 'My Task')
  await app.click('[data-testid="save"]')

  // Complete task
  await app.click('[data-testid="task"]')
  await app.click('[data-testid="complete"]')

  // Verify
  expect(await app.text('[data-testid="status"]')).toBe('Completed')

  await app.stop()
})
```

## Test Scenarios

| Scenario | Description |
|----------|------------|
| User Registration | Sign up flow |
| User Login | Login/logout |
| Create Task | Add new task |
| Update Task | Edit task |
| Delete Task | Remove task |
| Complete Task | Mark done |

## Running Tests

```bash
npm run test:e2e
```

## Best Practices

- One scenario per test
- Clean state between tests
- Use test data IDs