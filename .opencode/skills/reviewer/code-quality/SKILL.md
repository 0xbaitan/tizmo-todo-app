# Code Quality Skill

## Overview
Review code for quality, maintainability, and readability.

## Quality Checklist

- [ ] Readable naming
- [ ] DRY (Don't Repeat Yourself)
- [ ] Single responsibility
- [ ] Proper error handling
- [ ] Tests included

## Naming Conventions

```typescript
// BAD
const d = new Date()
const fn = () => {}

// GOOD
const currentDate = new Date()
const fetchTasks = () => {}
```

## DRY Principle

```typescript
// BAD
function formatDate(date: Date) {
  return date.toISOString().split('T')[0]
}
function formatTimestamp(date: Date) {
  return date.toISOString().split('T')[0]
}

// GOOD
function formatDate(date: Date) {
  return date.toISOString().split('T')[0]
}
```

## Error Handling

```typescript
// GOOD
try {
  const result = await riskyOperation()
  return { success: true, data: result }
} catch (error) {
  logger.error('Operation failed', { error })
  return { success: false, error: error.message }
}
```

## Comment Guidelines

- Explain WHY, not WHAT
- Complex logic needs comments
- Document edge cases

## Review Comment Format

```
[TYPE] Description

Explanation and suggestion.
```

Types: [BLOCKING], [REQUIRED], [SUGGESTION], [QUESTION], [PRAISE]