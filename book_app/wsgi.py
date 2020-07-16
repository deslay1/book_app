"""
WSGI config for book_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

""" path = '/Users/deslay/Documents/projects/book_app/book_app'
if path not in sys.path:
    sys.path.append(path) """

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_app.settings')

application = get_wsgi_application()
