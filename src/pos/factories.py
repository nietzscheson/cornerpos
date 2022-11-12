import factory
from django.contrib.auth import get_user_model

from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    _PASSWORD = "password123!"
    _COMMON_PASSWORD = "password123"

    password = factory.PostGenerationMethodCall("set_password", _PASSWORD)
    email = factory.Faker("email")
    username = factory.Faker("name")
    is_active = False
    is_staff = False
    is_superuser = False
