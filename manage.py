#!/usr/bin/env python
import os
import sys

def main():
    settings_module = (
        'girls_backend.settings_deployment'
        if 'RENDER_EXTERNAL_HOSTNAME' in os.environ
        else 'girls_backend.settings'
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
