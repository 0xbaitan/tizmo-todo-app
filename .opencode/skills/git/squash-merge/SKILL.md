---
name: git-squash-merge
description: Handle merge workflow with squash and branch cleanup
license: MIT
compatibility: "1.0"
---

# Merge Skill

## Overview
Handle merge workflow after PR approval with squash merging and branch cleanup.

## Merge Strategy

**Squash and Merge** (preferred):
- Creates single clean commit
- Preserves linear history
- Easy to revert

## Workflow

1. PR approved by reviewer
2. Squash and merge to develop/main
3. Delete feature branch
4. Update local branch

## Commands

```bash
# Squash merge via GitHub CLI
gh pr merge --admin --squash

# Or using standard git
git checkout develop
git merge --squash feature/branch
git commit -m "Merge branch"
git branch -d feature/branch
```

## Post-Merge Cleanup

```bash
# Update local develop
git checkout develop
git pull origin develop

# Delete remote feature branch
git push origin --delete feature/branch

# Delete local feature branch
git branch -d feature/branch
```

## Best Practices

- Always use squash merge for features
- Delete branch after merge
- Update local main/develop
- Verify build passes after merge