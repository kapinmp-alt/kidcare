"""
WSGI config for nanny_care project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nanny_care.settings')

# Ensure migrations are applied at startup so deployed instances have required tables.
# This helps on platforms where startup commands may not run migrations reliably.
try:
	# Import here to avoid heavy imports at module import time in some contexts
	from django.core.management import call_command
	call_command('migrate', '--noinput')
except Exception:
	# If migrations fail for any reason, don't crash the WSGI process here;
	# the error will appear in logs and can be investigated.
	pass

application = get_wsgi_application()
