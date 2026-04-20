# Integration Test Skill

## Overview
Design and write integration tests for component interactions and API endpoints.

## API Test Structure

```typescript
import request from 'supertest'
import { app } from '../src/app'

describe('Task API', () => {
  describe('POST /api/tasks', () => {
    it('should create task', async () => {
      const response = await request(app)
        .post('/api/tasks')
        .send({ title: 'Test Task' })
        .expect(201)

      expect(response.body.id).toBeDefined()
      expect(response.body.title).toBe('Test Task')
    })

    it('should return 400 for invalid data', async () => {
      const response = await request(app)
        .post('/api/tasks')
        .send({ title: '' })
        .expect(400)
    })
  })
})
```

## Database Integration

- Test with local DynamoDB
- Use test tables with `-test` suffix
- Clean up after each test

## Service Integration

- Test Lambda function calls
- Test S3 operations
- Test Cognito integration

## Running Tests

```bash
npm run test:api
```

## Best Practices

- Use Test Database
- Clean up between tests
- Mock external services