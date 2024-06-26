# Generated by Django 5.0.4 on 2024-04-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee_resume", "0003_rename_resume_name_resume_resume_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AffineModel",
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
                (
                    "token",
                    models.CharField(max_length=250, verbose_name="Affine Token"),
                ),
                (
                    "workspace",
                    models.CharField(max_length=50, verbose_name="Affine Workspace"),
                ),
            ],
        ),
    ]
