# Electron Skill

## Overview
Build Electron desktop apps with security, IPC, and system integration.

## Main Process

```javascript
const { app, BrowserWindow, ipcMain } = require('electron')

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      sandbox: true,
      preload: path.join(__dirname, 'preload.js')
    }
  })
}

app.whenReady().then(createWindow)
```

## Security

| Setting | Value |
|---------|-------|
| nodeIntegration | false |
| contextIsolation | true |
| sandbox | true |
| webSecurity | true |

## IPC Communication

```javascript
// Preload
contextBridge.exposeInMainWorld('api', {
  getTasks: () => ipcRenderer.invoke('get-tasks'),
  createTask: (data) => ipcRenderer.invoke('create-task', data)
})

// Main
ipcMain.handle('get-tasks', async (event, userId) => {
  return await fetchTasks(userId)
})
```

## Window Management

- Minimize, maximize, close
- Window state persistence
- Always on top option
- Frameless with custom titlebar

## System Integration

- System tray: `Tray` class
- Notifications: `Notification` class
- Global shortcuts: `globalShortcut`
- File dialogs: `dialog` module
- Menu: `Menu` class

## Build Configuration

```javascript
// electron-builder.json
{
  "appId": "com.tizmo.todo",
  "productName": "Tizmo Todo",
  "directories": {
    "output": "dist"
  },
  "mac": { "category": "public.app-category.productivity" },
  "win": { "target": "nsis" }
}
```