# UX Patterns Skill

## Overview
Provide design guidance for common user experience patterns.

## Usability Principles

1. **Visibility**: Keep users informed
2. **Control**: Allow undo/redo
3. **Consistency**: Follow conventions
4. **Feedback**: Show results
5. **Efficiency**: Shortcuts for experts

## Common Patterns

### Master-Detail

```
┌──────────────┬─────────────────┐
│ List        │ Detail View     │
│ - Item 1   │ [Selected Item] │
│ - Item 2 > │               │
│ - Item 3   │ Description   │
└──────────────┴─────────────────┘
```

### Modal Dialog

```
┌─────────────────────────┐
│ Title      [X]   │
├─────────────────────────┤
│                   │
│   Content         │
│                   │
├─────────────────────────┤
│ [Cancel] [Confirm] │
└─────────────────────────┘
```

### Form Layout

- Single column for mobile
- Labels above inputs
- Validation below fields
- Primary action right-aligned

### Empty States

```
┌─────────────────────────┐
│                         │
│      [Illustration]      │
│                         │
│   No Tasks Yet          │
│   Create your first   │
│   task to get started  │
│                         │
│  [+ Create Task]      │
└─────────────────────────┘
```

## Feedback Patterns

- Loading: Spinner or skeleton
- Success: Toast notification
- Error: Inline message + field highlight
- Info: Banner or tooltip