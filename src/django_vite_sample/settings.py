import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

# shortcut: dev-only settings (DEBUG on, fallback secret key), split per environment before deploying.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-dev-only")
DEBUG = True
ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    # "django_vite",
    "django_vite_sample.todos",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

ROOT_URLCONF = "django_vite_sample.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        # `request` lets the nav mark the current page.
        "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
    }
]

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"},
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

# The Svelte (Vite) dev server, when run side by side with Django.
CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "http://localhost:8000"]

# DJANGO_VITE = {"default": {"dev_mode": DEBUG}}

# STATICFILES_DIRS = [BASE_DIR / "frontend-app" / "dist"]
