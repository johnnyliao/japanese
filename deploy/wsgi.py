import sys
import os

PROJECT_ROOT = "/var/www/django/japanese"

# for project's apps
sys.path.append(PROJECT_ROOT)

# for settings.py
sys.path.append(os.path.dirname(PROJECT_ROOT))

# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % PROJECT_DIRNAME)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
