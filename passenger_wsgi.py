# -*- coding: utf-8 -*-
import os, sys

sys.path.insert(0, '/var/www/u0963683/data/maddynyan_server')
sys.path.insert(1, '/var/www/u0963683/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'maddynyan_server.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()