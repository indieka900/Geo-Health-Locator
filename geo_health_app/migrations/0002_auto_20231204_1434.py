# Generated by Django 3.2.23 on 2023-12-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_health_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatpatient',
            name='ip_op_number',
        ),
        migrations.AddField(
            model_name='treatpatient',
            name='op_number',
            field=models.IntegerField(default=1, verbose_name='OP Number'),
            preserve_default=False,
        ),
    ]
