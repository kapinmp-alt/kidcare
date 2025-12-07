import os

# Provide a top-level `app` callable so `gunicorn app:app` works if used.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nanny_care.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
# `gunicorn app:app` expects `app` attribute; make it an alias of `application`.
app = application
