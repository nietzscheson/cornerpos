"""
Creates the default Site object.
"""

from django.apps import apps as global_apps
from django.conf import settings
from django.core.management.color import no_style
from django.db import DEFAULT_DB_ALIAS, connections, router


def create_localhost_site(
    app_config,
    verbosity=2,
    interactive=True,
    using=DEFAULT_DB_ALIAS,
    apps=global_apps,
    **kwargs
):
    try:
        Site = apps.get_model("sites", "Site")
    except LookupError:
        return

    if not router.allow_migrate_model(using, Site):
        return

    if verbosity >= 2:
        print("Creating localhost:8000 Site object")
    Site(
        pk=getattr(settings, "SITE_ID", 1),
        domain="localhost:8000",
        name="localhost:8000",
    ).save(using=using)

    # We set an explicit pk instead of relying on auto-incrementation,
    # so we need to reset the database sequence. See #17415.
    sequence_sql = connections[using].ops.sequence_reset_sql(no_style(), [Site])
    if sequence_sql:
        if verbosity >= 2:
            print("Resetting sequence")
        with connections[using].cursor() as cursor:
            for command in sequence_sql:
                cursor.execute(command)
