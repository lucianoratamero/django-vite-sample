# django-vite-sample

Projeto de exemplo da palestra do **PythOnSerra** sobre como servir um frontend moderno (Svelte +
Vite) a partir do Django, usando o [django-vite](https://github.com/MrBin99/django-vite).

É a mesma lista de tarefas feita de dois jeitos, lado a lado, sobre o mesmo banco de dados:

| | Django puro | Svelte + Vite |
|---|---|---|
| Onde roda | http://localhost:8000 | http://localhost:5173 |
| Como renderiza | Templates do Django, formulários HTML, sem JavaScript | SPA em Svelte 5 que conversa com a API REST |
| Estilo | CSS puro, paleta ameixa e rosa (`todos/static/todos/site.css`) | Tailwind CSS 4, paleta da [Lincoln Loop](https://lincolnloop.com) (`frontend-app/src/app.css`) |

As cores são diferentes de propósito, pra ficar fácil saber em qual versão você está. Já a fonte
([Allo](https://allo.joshpuckett.me)), os tamanhos e os espaçamentos são os mesmos nas duas.

## Stack

- **Backend:** Python 3.13+, Django 6, Django REST framework, django-cors-headers, django-vite
- **Frontend:** Svelte 5 (runes), Vite 8, Tailwind CSS 4 + typography, sv-router, TypeScript
- **Ferramentas:** [uv](https://docs.astral.sh/uv/), ruff, npm,
  [oxfmt](https://oxc.rs/docs/guide/usage/formatter), ESLint

## Estrutura

```
src/django_vite_sample/       projeto Django (settings, urls)
└── todos/                    app de tarefas: model, API, views, templates, testes
    ├── static/todos/         CSS e fonte das páginas Django
    └── templates/todos/      base.html, todo_list.html, about.html
frontend-app/                 app Svelte + Vite
└── src/                      App.svelte, Todos.svelte, About.svelte, app.css
```

## Rodando localmente

Você vai precisar de [uv](https://docs.astral.sh/uv/) e Node.js (as versões usadas estão em
`.tool-versions`).

Se você usa o [asdf](https://asdf-vm.com), é só ativar os plugins do Node.js e do Python e rodar
`asdf install` pra ter os dois nas versões certas:

```sh
asdf plugin add nodejs
asdf plugin add python
asdf install
```

Na primeira vez, instale as dependências, crie o banco e o `frontend-app/.env` (o `VITE_API_HOST`
aponta pro Django em :8000):

```sh
make setup
```

Depois, suba os dois servidores juntos:

```sh
make dev   # Django em http://localhost:8000 e Vite em http://localhost:5173
```

Um Ctrl+C para os dois. `make django` e `make vite` sobem só um deles. O uv não tem um executor de
tarefas como os scripts do npm, por isso o `Makefile`.

Abra o Svelte em `localhost:5173`, não em `127.0.0.1:5173`: o CORS do Django só libera
`localhost`.

## Rotas

| Rota | O que é |
|---|---|
| `/` e `/about/` (Django) | Lista de tarefas e página "sobre", renderizadas pelo Django |
| `/` e `/about` (Svelte) | As mesmas páginas, renderizadas pelo Svelte |
| `GET`, `POST` `/api/todos/` | Lista e cria tarefas |
| `GET`, `PATCH`, `PUT`, `DELETE` `/api/todos/<id>/` | Lê, atualiza e apaga uma tarefa |

## Integração com o django-vite

Hoje os dois apps rodam separados: o Django na porta 8000 e o servidor do Vite na 5173. Os passos
pra o Django servir o app Svelte com o django-vite estão comentados no código:

- `src/django_vite_sample/settings.py`: `django_vite` no `INSTALLED_APPS`, `DJANGO_VITE` e
  `STATICFILES_DIRS` apontando pro build do Vite
- `frontend-app/vite.config.ts`: `base` e o `manifest` do build
- `src/django_vite_sample/todos/templates/todos/base.html`: um template com as tags
  `{% vite_hmr_client %}` e `{% vite_asset %}`

## Testes e qualidade

```sh
uv run python manage.py test django_vite_sample.todos
uv run ruff check && uv run ruff format --check

cd frontend-app
npm run check   # svelte-check / TypeScript
npm run lint    # oxfmt + ESLint
```

## Fonte

A [Allo](https://allo.joshpuckett.me), de Josh Puckett, é distribuída sob a SIL Open Font License
1.1. O Svelte usa o pacote npm `allo-font`. O Django usa uma cópia do mesmo arquivo em
`todos/static/todos/fonts/`, junto com a licença. Tudo funciona offline.
