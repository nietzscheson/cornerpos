# Generated by Django 3.2.7 on 2021-09-23 22:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("option_1", models.CharField(max_length=100)),
                ("option_2", models.CharField(max_length=100)),
                ("option_3", models.CharField(max_length=100)),
                ("option_4", models.CharField(max_length=100)),
                ("date_at", models.DateField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
