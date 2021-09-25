from uuid import uuid4
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import localdate
from django.contrib.auth import get_user_model
from django_currentuser.db.models import CurrentUserField
from pos.validators import validate_date


class ResourceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menu(ResourceModel):
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    date_at = models.DateField(validators=[validate_date])


class Order(ResourceModel):
    class MenuOptions(models.TextChoices):
        OPTION_1 = "OPTION_1", "Option 1"
        OPTION_2 = "OPTION_2", "Option 2"
        OPTION_3 = "OPTION_3", "Option 3"
        OPTION_4 = "OPTION_4", "Option 4"

    user = CurrentUserField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    option = models.CharField(max_length=100, choices=MenuOptions.choices)
    preference = models.CharField(max_length=100, blank=True, null=True)
