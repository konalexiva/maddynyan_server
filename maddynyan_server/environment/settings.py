import os

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = [
    os.getenv('MACHINE_HOST', '127.0.0.1'),
    os.getenv('HOST_IP', '127.0.0.1'),
    os.getenv('HOST_DOMAIN', '127.0.0.1'),
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'konalexiva'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'gopaslona'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': '5432',
    },

}
