# Generated by Django 3.2.23 on 2023-11-15 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geo_health_app', '0004_alter_disease_symptoms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='reporter',
        ),
        migrations.AddField(
            model_name='disease',
            name='reporter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
