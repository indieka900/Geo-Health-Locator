# Generated by Django 3.2.23 on 2023-12-04 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_health_app', '0003_alter_treatpatient_op_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatpatient',
            old_name='op_number',
            new_name='ip_op_number',
        ),
    ]
