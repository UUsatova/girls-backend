import os

import dj_database_url

from .settings import *  # noqa: F403,F401

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise RuntimeError('DJANGO_SECRET_KEY is required')

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')
    if host.strip()
]
if not ALLOWED_HOSTS and os.getenv('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS = [os.getenv('RENDER_EXTERNAL_HOSTNAME')]
if not ALLOWED_HOSTS:
    raise RuntimeError('DJANGO_ALLOWED_HOSTS is required')

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')
    if origin.strip()
]
if not CSRF_TRUSTED_ORIGINS and os.getenv('RENDER_EXTERNAL_HOSTNAME'):
    CSRF_TRUSTED_ORIGINS = [f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}"]

CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')
    if origin.strip()
]

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError('DATABASE_URL is required')

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = os.getenv('DJANGO_SECURE_SSL_REDIRECT', '1') == '1'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}
