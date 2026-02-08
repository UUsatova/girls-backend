import os
from django.core.wsgi import get_wsgi_application

settings_module = (
    'girls_backend.settings_deployment'
    if 'RENDER_EXTERNAL_HOSTNAME' in os.environ
    else 'girls_backend.settings'
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
