from django.apps import AppConfig
from django.contrib.sites.checks import check_site_id
from django.core import checks
from django.db.models.signals import post_migrate
from pos.management import create_localhost_site


class PosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pos"

    def ready(self):
        post_migrate.connect(create_localhost_site, sender=self)
        checks.register(check_site_id, checks.Tags.sites)
