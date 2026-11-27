.PHONY: setup dev django vite

setup:
	uv sync
	uv run python manage.py migrate
	npm --prefix ./frontend-app install
	cp ./frontend-app/.env.example ./frontend-app/.env   # VITE_API_HOST aponta pro Django em :8000

# Django (:8000) and Vite (:5173) side by side. Ctrl+C stops both.
dev:
	$(MAKE) -j2 django vite

django:
	uv run python manage.py runserver

vite:
	cd frontend-app && npm run dev
