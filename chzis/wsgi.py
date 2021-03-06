"""
WSGI config for chzis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import sys
import os


sys.path.append('/home/www/chzis')
sys.path.append('/home/www/chzis/chzis')

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chzis.settings")

application = get_wsgi_application()
