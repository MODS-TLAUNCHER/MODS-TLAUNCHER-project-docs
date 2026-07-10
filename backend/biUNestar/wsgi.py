"""
WSGI config for biUNestar project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biUNestar.settings')
application = get_wsgi_application()