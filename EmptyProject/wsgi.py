import os
import sys
from django.core.wsgi import get_wsgi_application

from EmptyProject.settings import VIRTUALENV_PATH

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmptyProject.settings')
sys.path.append(VIRTUALENV_PATH)
application = get_wsgi_application()
