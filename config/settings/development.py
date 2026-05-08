"""Development settings — debug mode, toolbar, relaxed security."""
from .base import *  # noqa: F401, F403

DEBUG = True
INTERNAL_IPS = ["127.0.0.1"]

try:
    import debug_toolbar  # noqa: F401
    INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
except ImportError:
    pass
