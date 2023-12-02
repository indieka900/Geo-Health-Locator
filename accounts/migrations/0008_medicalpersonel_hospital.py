# Generated by Django 3.2.23 on 2023-12-02 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalpersonel',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.hospital'),
        ),
    ]
