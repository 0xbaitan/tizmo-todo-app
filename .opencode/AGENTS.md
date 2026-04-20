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

## Apps Folder

Multi-package applications reside in the `/apps/` folder at the project root.

### Structure

```
apps/
└── desktop/          # Vite + Electron + TypeScript
    ├── src/          # Renderer (Vite frontend)
    ├── electron/     # Electron main process
    ├── vite.config.ts
    ├── forge.config.ts
    └── package.json
```

### Rules

1. **Location**: All applications go in `apps/` folder
2. **Package manager**: Use `bun` for all apps
3. **No git**: Do not initialize git inside app folders (parent .git tracks them)
4. **Testing**: Each app should have its own test setup
5. **Dependencies**: Install via `bun install` in app directory
