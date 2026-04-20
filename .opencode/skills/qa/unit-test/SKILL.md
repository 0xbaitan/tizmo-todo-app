# Unit Test Skill

## Overview
Design and write unit tests for individual functions and components.

## Test Structure

```typescript
describe('TaskService', () => {
  describe('createTask', () => {
    it('should create task with valid data', async () => {
      // Arrange
      const taskData = { title: 'Test', userId: 'user-1' }

      // Act
      const task = await TaskService.create(taskData)

      // Assert
      expect(task.id).toBeDefined()
      expect(task.title).toBe('Test')
    })
  })
})
```

## AAA Pattern

1. **Arrange**: Set up test data
2. **Act**: Execute the function
3. **Assert**: Verify the result

## Naming

```
should [expected behavior] when [condition]
```

Examples:
- `should return task when valid data provided`
- `should throw error when title is empty`

## Mocking

```typescript
jest.mock('../lib/dynamodb', () => ({
  docClient: {
    put: jest.fn().mockReturnValue({ promise: () => ({}) }),
    get: jest.fn()
  }
}))
```

## Running Tests

```bash
npm test              # All tests
npm test -- --coverage  # With coverage
npm test -- --watch   # Watch mode
```

## Coverage Goals

- Minimum 80% overall
- Critical paths: 100%
- New code: 100%