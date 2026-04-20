# Next.js Skill

## Overview
Build Next.js applications with App Router, SSR, and API routes.

## Project Structure

```
src/
├── app/
│   ├── layout.tsx      # Root layout
│   ├── page.tsx        # Home page
│   └── tasks/
│       ├── page.tsx    # Tasks list
│       └── [id]/page.tsx
├── components/
│   ├── TaskList.tsx
│   └── TaskForm.tsx
└── lib/
    └── api.ts
```

## Page Component

```tsx
export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([])

  useEffect(() => {
    fetch('/api/tasks')
      .then(res => res.json())
      .then(setTasks)
  }, [])

  return (
    <div>
      <h1>Tasks</h1>
      <TaskList tasks={tasks} />
    </div>
  )
}
```

## API Route

```typescript
// src/app/api/tasks/route.ts
export async function GET(request: Request) {
  const user = await authenticate(request)
  const tasks = await getTasks(user.id)
  return Response.json(tasks)
}

export async function POST(request: Request) {
  const user = await authenticate(request)
  const data = await request.json()
  const task = await createTask(user.id, data)
  return Response.json(task, { status: 201 })
}
```

## State Management

- React Context for auth
- SWR/React Query for data fetching
- Local state with useState

## Styling

- Tailwind CSS preferred
- CSS Modules for scoped styles
- Follow design system tokens

## Build & Run

```bash
npm run dev    # Development
npm run build # Production build
npm start     # Production server
```