import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

CELERY_CONFIG = {
    "BROKER_URL": os.environ.get("BROKER_URL"),
    "BROKER_TRANSPORT": "redis",
}

app.conf.update(**CELERY_CONFIG)
app.autodiscover_tasks()
