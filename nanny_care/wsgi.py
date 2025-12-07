"""
WSGI config for nanny_care project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys
import traceback

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nanny_care.settings')

# Attempt to run migrations at startup so deployed instances have required tables.
# Log any errors to stderr so the hosting service captures them in logs.
try:
	from django.core.management import call_command
	print('Running migrations at WSGI startup...', file=sys.stderr)
	call_command('migrate', '--noinput')
	print('Migrations complete.', file=sys.stderr)
except Exception:
	print('Error running migrations at WSGI startup:', file=sys.stderr)
	traceback.print_exc(file=sys.stderr)

application = get_wsgi_application()
