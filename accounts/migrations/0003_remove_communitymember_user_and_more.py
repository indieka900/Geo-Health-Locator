# Generated by Django 4.2.6 on 2023-11-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_identification"),
    ]

    operations = [
        migrations.RemoveField(model_name="communitymember", name="user",),
        migrations.RemoveField(model_name="medicalpersonel", name="user",),
        migrations.AddField(
            model_name="user",
            name="county",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="county"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="location"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="sub_county",
            field=models.CharField(
                blank=True, max_length=80, null=True, verbose_name="sub county"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="sub_location",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="sub location"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="village",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="village"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="ward",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="ward"
            ),
        ),
        migrations.DeleteModel(name="Administrator",),
        migrations.DeleteModel(name="CommunityMember",),
        migrations.DeleteModel(name="MedicalPersonel",),
    ]