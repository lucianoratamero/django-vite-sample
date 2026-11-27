.PHONY: setup dev django vite

setup:
	uv sync
	uv run python manage.py migrate
	# Superusuário admin:admin, só pra dev. Não recria (nem troca a senha) se já existir.
	uv run python manage.py shell -v 0 -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', password='admin')"
	npm --prefix ./frontend-app install
	cp ./frontend-app/.env.example ./frontend-app/.env   # VITE_API_HOST aponta pro Django em :8000

# Django (:8000) and Vite (:5173) side by side. Ctrl+C stops both.
dev:
	$(MAKE) -j2 django vite

django:
	uv run python manage.py runserver

vite:
	cd frontend-app && npm run dev
