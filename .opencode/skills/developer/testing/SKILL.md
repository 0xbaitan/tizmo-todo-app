# Testing Skill

## Overview
Write tests following the testing pyramid: unit, integration, and E2E.

## Test Framework

- **Unit**: Jest
- **Integration**: Supertest
- **E2E**: Playwright with Spectron

## Unit Test

```typescript
describe('TaskService', () => {
  describe('createTask', () => {
    it('should create task with valid data', async () => {
      const task = await TaskService.create({
        title: 'Test Task',
        userId: 'user-123'
      })
      expect(task.id).toBeDefined()
      expect(task.title).toBe('Test Task')
    })

    it('should throw with empty title', async () => {
      await expect(TaskService.create({ title: '' }))
        .rejects.toThrow('Title required')
    })
  })
})
```

## Integration Test

```typescript
describe('Task API', () => {
  it('should create and retrieve task', async () => {
    const create = await request(app)
      .post('/api/tasks')
      .send({ title: 'Test' })
      expect(create.status).toBe(201)

    const get = await request(app)
      .get(`/api/tasks/${create.body.id}`)
    expect(get.status).toBe(200)
    expect(get.body.title).toBe('Test')
  })
})
```

## E2E Test

```typescript
test('create and complete task', async () => {
  await app.start()
  await app.click('[data-testid="add-task"]')
  await app.fill('[data-testid="title"]', 'My Task')
  await app.click('[data-testid="save"]')
  await app.waitFor('[data-testid="task-list"]')
  await app.click('[data-testid="complete"]')
  expect(await app.text('[data-testid="status"]')).toBe('Completed')
  await app.stop()
})
```

## Running Tests

```bash
npm test              # Unit tests
npm run test:api    # Integration
npm run test:e2e    # E2E
npm run test:coverage
```

## Best Practices

- Follow AAA: Arrange, Act, Assert
- One logical assertion per test
- Mock external dependencies
- Test error paths