# frontend-app

The todo app's frontend: Svelte 5 + Vite + Tailwind CSS 4. It talks to the Django REST API at
`/api/todos/`.

```sh
npm install
cp .env.example .env  # VITE_API_HOST = Django's origin, when Django runs separately
npm run dev           # http://localhost:5173, with Django's runserver on :8000
```

- `npm run build` writes the static site to `dist/`. Serve it so unknown paths (like `/about`)
  fall back to `index.html`.
- `npm run check` type-checks, `npm run lint` / `npm run format` run Prettier and ESLint.
