from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Home app — landing page and public-facing pages."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.home"
    label = "home"
