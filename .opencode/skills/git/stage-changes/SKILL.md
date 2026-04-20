---
name: git-stage-changes
description: Stage files and prepare for manual commit approval
license: MIT
compatibility: "1.0"
---

# Commit Skill

## Overview
Stage changes and prepare for manual commit approval. NEVER auto-commit without user explicit approval.

## Workflow

1. Run `git status` - show changed files
2. Run `git diff` - show actual changes
3. Wait for user approval
4. User runs the commit command

## Commit Message Format

```
[type/TASK-number] Description

Optional body with more detail.
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `chore`: Maintenance
- `refactor`: Refactoring
- `test`: Tests
- `perf`: Performance

### Examples

```
[feat/TASK-123] Add user authentication
[fix/TASK-456] Fix task delete error
[docs/TASK-789] Update README with setup instructions
[chore/TASK-101] Update npm dependencies
```

## Commands

```bash
# Show status
git status

# Show diff
git diff
git diff --staged

# Stage files
git add filename
git add .
git add -p filename  # Partial staging

# Commit (user runs this)
git commit -m "[feat/TASK-123] Description"

# Amend last commit
git commit --amend
```

## Manual Approval Flow

```
Agent: "Files changed: src/app.ts, src/utils.ts"
Agent: "Diff:"
Agent: (shows git diff output)
Agent: "Ready to stage? Say 'yes' to stage, or specify files."

User: "yes"
Agent: "Staged files. Ready to commit?"
User: "yes, commit with: [feat/TASK-123] Add user auth"
Agent: "Run: git commit -m \"[feat/TASK-123] Add user auth\""
```

## Constraints

- NEVER commit without user approval
- Always show diff before staging
- Keep subject under 72 characters
- Reference task numbers