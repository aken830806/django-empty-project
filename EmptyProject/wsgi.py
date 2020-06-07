"""
WSGI config for EmptyProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
os.environ["DJANGO_SETTINGS_MODULE"] = "EmptyProject.settings"

import sys
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
from EmptyProject.settings import VIRTUALENV_PATH
sys.path.append(VIRTUALENV_PATH)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
