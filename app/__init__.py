import os

# Expose a WSGI callable as `app` on the `app` package so commands like
# `gunicorn app:app` succeed even when a package named `app` exists.
# We avoid calling `get_wsgi_application()` at import time because that
# triggers `django.setup()`; if this module is imported during Django's
# own setup (e.g. manage.py commands), it can cause a reentrant
# `populate()` error. Instead we create a lazy wrapper that initializes
# the real WSGI application on first request.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nanny_care.settings')


class _LazyWSGI:
	def __init__(self):
		self._app = None

	def _load(self):
		if self._app is None:
			from django.core.wsgi import get_wsgi_application
			self._app = get_wsgi_application()

	def __call__(self, environ, start_response):
		self._load()
		return self._app(environ, start_response)


# `gunicorn app:app` expects attribute `app`; provide a lazy callable.
app = _LazyWSGI()
# Also expose `application` for callers expecting that name.
application = app
