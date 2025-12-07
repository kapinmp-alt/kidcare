import os

# Expose a WSGI callable as `app` on the `app` package so commands like
# `gunicorn app:app` succeed even when a package named `app` exists.
# If `DJANGO_SETTINGS_MODULE` is not set by the environment, default to
# the project's settings (safe for Render where we set env vars).
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nanny_care.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
# `gunicorn app:app` expects attribute `app`; provide it as alias.
app = application
