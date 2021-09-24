from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


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
    date_at = models.DateField()

    def get_absolute_url(self):
        return reverse("pos:detail", kwargs={"pk": self.pk})
