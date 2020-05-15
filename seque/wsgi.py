"""
WSGI config for seque project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import socketio

import os
from backend.socketView import sio

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seque.settings')

django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)
