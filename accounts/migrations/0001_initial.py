# Generated by Django 4.2.6 on 2023-11-06 02:50

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=150, verbose_name="first name"),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="middle name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="last name"),
                ),
                ("identification", models.IntegerField(verbose_name="identification")),
                (
                    "email",
                    models.EmailField(
                        error_messages={"unique": "A user with email already exists."},
                        max_length=254,
                        unique=True,
                        verbose_name="email",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=10,
                        verbose_name="gender",
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=27,
                        null=True,
                        region=None,
                        unique=True,
                        verbose_name="phone number",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Administrator", "Administrator"),
                            ("Community Member", "Community Member"),
                            ("Medical Personel", "Medical Personel"),
                        ],
                        max_length=17,
                        verbose_name="Role",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                ("is_admin", models.BooleanField(default=False, verbose_name="admin")),
                ("is_staff", models.BooleanField(default=False, verbose_name="staff")),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="timestamp"),
                ),
            ],
            options={"abstract": False,},
        ),
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
                    "email",
                    models.EmailField(
                        error_messages={"unique": "A user with email already exists!"},
                        max_length=254,
                        unique=True,
                        verbose_name="email",
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
                    "county",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="county"
                    ),
                ),
                (
                    "sub_county",
                    models.CharField(
                        blank=True, max_length=80, null=True, verbose_name="sub county"
                    ),
                ),
                (
                    "ward",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="ward"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="location"
                    ),
                ),
                (
                    "village",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="village"
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
                    "first_name",
                    models.CharField(max_length=50, verbose_name="first name"),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="middle name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="last name"),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True, max_length=80, null=True, verbose_name="county"
                    ),
                ),
                (
                    "sub_county",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="sub county"
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
