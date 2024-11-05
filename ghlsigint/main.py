import os

# We set the DJANGO_SETTINGS_MODULE here because main.py is only the entry point on a deployed site
# and doesn't get used locally.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ghlsigint.settings.production')

from ghlsigint.wsgi import application
app = application
