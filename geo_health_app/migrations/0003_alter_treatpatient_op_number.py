# Generated by Django 3.2.23 on 2023-12-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_health_app', '0002_auto_20231204_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatpatient',
            name='op_number',
            field=models.IntegerField(unique=True, verbose_name='OP Number'),
        ),
    ]
