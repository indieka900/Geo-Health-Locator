# Generated by Django 4.2.6 on 2023-11-07 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_user_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicalPersonel",
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
                ("bio", models.TextField(blank=True, null=True, verbose_name="bio")),
                (
                    "profile_picture",
                    models.ImageField(
                        default="default.png",
                        upload_to="profile",
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "kmdb_number",
                    models.CharField(max_length=100, verbose_name="KMDB Number"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="CommunityMember",
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
                ("bio", models.TextField(blank=True, null=True, verbose_name="bio")),
                (
                    "profile_picture",
                    models.ImageField(
                        default="default.png",
                        upload_to="profile",
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Administrator",
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
                ("bio", models.TextField(blank=True, null=True, verbose_name="bio")),
                (
                    "profile_picture",
                    models.ImageField(
                        default="default.png",
                        upload_to="profile",
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
