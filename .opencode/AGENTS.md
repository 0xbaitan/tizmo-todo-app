# Agents

This file defines rules and conventions for automated agents in this project.

## Scripts Folder

All automation scripts must reside in the `/scripts/` folder in the project root.

### Rules

1. **Location**: All scripts go in `scripts/` folder
2. **Self-contained**: Scripts must have no external dependencies beyond standard tools (bash, git, bun, etc.)
3. **Documentation**: Each script must have a header comment describing its purpose
4. **Taskfile Integration**: Link scripts to Taskfile.yml via `cmds` or `deps`
5. **Portability**: Use `#!/usr/bin/env bash` shebang
6. **Executable**: Scripts must have execute permission (`chmod +x`)

### Example Structure

```
scripts/
├── install.sh          # Installation script
├── upgrade.sh          # Upgrade script
└── Taskfile.yml        # Links to these scripts
```

### Taskfile Integration

```yaml
tasks:
  install:
    deps: [./scripts/install.sh]

  upgrade:
    cmds:
      - ./scripts/upgrade.sh
```