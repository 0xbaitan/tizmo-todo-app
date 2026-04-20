# Accessibility Skill

## Overview
Provide design guidance for accessible UI following WCAG guidelines.

## WCAG Guidelines

### Color Contrast

- Text: Minimum 4.5:1 ratio
- Large text: Minimum 3:1 ratio
- UI components: Minimum 3:1

### Focus States

```css
/* Visible focus indicator */
:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}
```

### Keyboard Navigation

- All interactive elements accessible via keyboard
- Logical tab order
- Skip links for main content

### Screen Reader

- Proper ARIA labels
- Semantic HTML
- Meaningful alt text

## ARIA Labels

```tsx
<button aria-label="Add new task">
  <PlusIcon />
</button>

<input
  aria-label="Task title"
  aria-required="true"
/>

<div role="alert" aria-live="polite">
  Task created successfully
</div>
```

## Best Practices

| Principle | Implementation |
|-----------|----------------|
| Keyboard | Tab order, focus states |
| Screen reader | ARIA, semantic HTML |
| Color | Not sole indicator |
| Motion | Respect prefers-reduced-motion |