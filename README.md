# ORYGIN Kampus — Site Vitrine

Site vitrine de l'organisme de formation et d'insertion professionnelle **ORYGIN Kampus**, ancré en Guyane française.

## Stack technique

- **Backend** : Django 5.2 LTS
- **Templates** : Django Template Language
- **CSS** : Tailwind CSS (Play CDN en dev, CLI en prod)
- **JS** : Vanilla JS
- **Gestion des dépendances** : [uv](https://github.com/astral-sh/uv)
- **Serveur de fichiers statiques** : Whitenoise

## Prérequis

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

```bash
git clone git@github.com:codeforge14/orygin-kampus.git
cd orygin-kampus

cp .env.example .env
# Éditer .env et renseigner SECRET_KEY

uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Le site est accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Structure du projet

```
site_vitrine/
├── apps/
│   └── home/           # App landing page
├── config/
│   └── settings/       # base / development / production / testing
├── static/
│   ├── css/            # custom.css
│   ├── images/         # logo et assets
│   └── js/             # main.js
├── templates/
│   ├── base.html       # Layout principal (nav + footer)
│   └── home.html       # Page d'accueil
├── .env.example
├── manage.py
├── pyproject.toml
└── tailwind.config.js
```

## Variables d'environnement

| Variable | Description | Exemple |
|---|---|---|
| `SECRET_KEY` | Clé secrète Django | `django-insecure-...` |
| `DEBUG` | Mode debug | `True` / `False` |
| `ALLOWED_HOSTS` | Hôtes autorisés | `localhost,127.0.0.1` |
| `DATABASE_URL` | URL de la base de données | `sqlite:///db.sqlite3` |

## Commandes utiles

```bash
uv run python manage.py migrate          # Appliquer les migrations
uv run python manage.py collectstatic    # Collecter les fichiers statiques
uv sync --extra dev                      # Installer les dépendances de dev
uv run pytest                            # Lancer les tests
```

## Déploiement

Voir `config/settings/production.py` pour la configuration production (HTTPS, HSTS, Argon2).

```bash
DJANGO_SETTINGS_MODULE=config.settings.production uv run python manage.py collectstatic
```
