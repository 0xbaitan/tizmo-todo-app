---
name: create-pr
description: Create pull requests with proper title, description, labels
license: MIT
compatibility: '1.0'
---

# PR Skill

## Overview

Create pull requests with proper title, description, and labels. Link to tasks.

## PR Title Format

```
[type/TASK-number] Description
```

Examples:

```
[feat/TASK-123] Add user authentication
[fix/TASK-456] Fix task delete error
```

## PR Description Template

```markdown
## Summary

Brief description of changes

## Changes

- List of changes

## Testing

How tested

## Checklist

- [ ] Tests pass
- [ ] Lint passes
- [ ] Manual testing done
```

## Commands

```bash
# Push branch
git push -u origin branch-name

# Create PR (via gh CLI)
gh pr create --title "[feat/TASK-123] Add auth" --body file.md

# List PRs
gh pr list

# View PR
gh pr view 123
```

## Labels

Add relevant labels:

- `enhancement`
- `bug`
- `documentation`
- `needs-review`

## Best Practices

- Small PRs are better
- Tests must pass
- Include description
- Link to task
