# Generated by Django 3.2.23 on 2023-11-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_health_app', '0005_auto_20231115_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='reported_to',
            field=models.CharField(default='Mwatate Sub-County Hospital', max_length=50, verbose_name='Reported to'),
        ),
    ]