"""
WSGI config for ghlsigint project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import logging

from django.core.wsgi import get_wsgi_application
from djangae.environment import is_production_environment
import google.cloud.logging


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ghlsigint.settings.default')


if is_production_environment():
    try:
        # Instantiates a client
        client = google.cloud.logging.Client()

        # Retrieves a Cloud Logging handler based on the environment
        # you're running in and integrates the handler with the
        # Python logging module. By default this captures all logs
        # at INFO level and higher
        client.get_default_handler()
        client.setup_logging()
        logging.info("Cloud logging setup")
    except google.auth.exceptions.DefaultCredentialsError:
        logging.warning(
            "Unable to find credentials for Google Cloud logging configuration"
        )
        pass

    try:
        import googleclouddebugger
        googleclouddebugger.enable(breakpoint_enable_canary=False)
    except google.auth.exceptions.DefaultCredentialsError:
        logging.warning(
            "Unable to find credentials for Google Cloud debugging"
        )
    except ImportError:
        pass

application = get_wsgi_application()
