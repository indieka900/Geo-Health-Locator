# Generated by Django 4.2.6 on 2023-11-09 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Disease",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symptoms", models.JSONField(default=list)),
                (
                    "latitude",
                    models.FloatField(blank=True, null=True, verbose_name="latitude"),
                ),
                (
                    "longitude",
                    models.FloatField(blank=True, null=True, verbose_name="longitude"),
                ),
                ("reported_at", models.DateTimeField(auto_now_add=True)),
                (
                    "reporter",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "disease_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="geo_health_app.disease",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=100, verbose_name="full name"),
                ),
                ("age", models.IntegerField(blank=True, null=True, verbose_name="age")),
                (
                    "health_situation",
                    models.TextField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="health situation",
                    ),
                ),
            ],
            bases=("geo_health_app.disease",),
        ),
    ]