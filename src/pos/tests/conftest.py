import pytest

from django.core.management import call_command


@pytest.fixture()
def loaddata(django_db_setup, django_db_blocker ):
    def _(fixture={}):
        with django_db_blocker.unblock():
            call_command('loaddata', *fixture)
    return _
