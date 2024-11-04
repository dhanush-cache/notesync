import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notesync.settings")
django.setup()
