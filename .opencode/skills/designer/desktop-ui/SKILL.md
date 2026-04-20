# Desktop UI Skill

## Overview
Provide design guidance specific to desktop application interfaces.

## Window Management

- Proper minimize/maximize/close buttons
- Window position and size persistence
- Multi-window support
- Native window chrome preferred

## System Integration

- System tray icon with menu
- Global shortcuts
- Desktop notifications
- Native menus

## Layout

```
┌─────────────────────────────────────┐
│ [─][□][X]  App Title      │ <- Title Bar
├─────────────────────────────────────┤
│ File  Edit  View  Help   │ <- Menu Bar
├────────┬────────────────────────────┤
│        │                            │
│ Nav    │   Main Content            │
│        │                            │
│ - All  │   ┌──────────────────┐   │
│ - Work │   │ Task List        │   │
│ - Done │   └──────────────────┘   │
│        │                            │
├────────┴────────────────────────────┤
│ Status: 3 tasks │ v1.0.0           │ <- Status Bar
└─────────────────────────────────────┘
```

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| New Task | Ctrl+N |
| Save | Ctrl+S |
| Search | Ctrl+F |
| Settings | Ctrl+, |
| Quit | Ctrl+Q |

## Desktop-Specific

- Right-click context menus
- Drag and drop support
- Tooltips on hover
- Double-click actions