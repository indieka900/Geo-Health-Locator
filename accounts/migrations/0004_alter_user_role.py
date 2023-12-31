# Generated by Django 4.2.6 on 2023-11-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_communitymember_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("Administrator", "Administrator"),
                    ("Community Member", "Community Member"),
                    ("Medical Personel", "Medical Personel"),
                ],
                default="Community Member",
                max_length=17,
                verbose_name="Role",
            ),
        ),
    ]
