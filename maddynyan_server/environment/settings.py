import os

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = [
    os.getenv('MACHINE_HOST', '127.0.0.1'),
    os.getenv('HOST_IP', '127.0.0.1'),
    os.getenv('HOST_DOMAIN', '127.0.0.1'),
    'maddynyan.ru',
    'www.maddynyan.ru'
]
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME', 'db-name'),
#         'USER': os.getenv('DB_USER', 'db-user'),
#         'PASSWORD': os.getenv('DB_PASSWORD', 'db-password'),
#         'HOST': os.getenv('DB_HOST', '127.0.0.1'),
#         'PORT': '5432',
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maddynyan_db',
        'USER': 'konalexiva',
        'PASSWORD': 'gopaslona',
        'HOST': '194.58.103.153',
        'PORT': '5432',
    },
}
