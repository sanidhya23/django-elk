import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_elk.settings")
app = Celery("django_elk")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()