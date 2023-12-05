# Generated by Django 3.2.23 on 2023-12-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_health_app', '0004_rename_op_number_treatpatient_ip_op_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='type',
            field=models.CharField(choices=[('Ambulance', 'Ambulance'), ('Disease', 'Disease')], default='Disease', max_length=20, verbose_name='Submision type'),
        ),
    ]