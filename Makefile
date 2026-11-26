.PHONY: dev django vite

# Django (:8000) and Vite (:5173) side by side. Ctrl+C stops both.
dev:
	$(MAKE) -j2 django vite

django:
	uv run python manage.py runserver

vite:
	cd frontend-app && npm run dev
