import os
import sys
from os.path import dirname, abspath
from django.core.wsgi import get_wsgi_application

from EmptyProject.settings import VIRTUALENV_PATH

os.environ["DJANGO_SETTINGS_MODULE"] = "EmptyProject.settings"
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
sys.path.append(VIRTUALENV_PATH)
application = get_wsgi_application()
