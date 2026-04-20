# Branch Skill

## Overview
Create and manage GitFlow branches with proper naming convention.

## Branch Types

| Type | Purpose | Base |
|------|--------|------|
| feat/ | New features | develop |
| fix/ | Bug fixes | develop |
| docs/ | Documentation | develop |
| chore/ | Maintenance | develop |
| refactor/ | Code refactoring | develop |
| test/ | Test additions | develop |
| perf/ | Performance | develop |
| hotfix/ | Urgent production fixes | main |

## Branch Naming

```
feat/TASK-123-user-authentication
fix/TASK-456-task-delete-error
docs/TASK-789-readme-update
```

Format: `<type>/<TASK-number>-<description>`

## Commands

```bash
# Create branch from develop
git checkout -b feat/TASK-123-description develop

# Create branch from main (hotfix)
git checkout -b hotfix/TASK-789-urgent-fix main

# List branches
git branch -a

# Delete local branch
git branch -d branch-name

# Delete remote branch
git push origin --delete branch-name
```

## Best Practices

- Branch from correct base
- Include task/ticket number
- Use kebab-case for description
- Delete after merge