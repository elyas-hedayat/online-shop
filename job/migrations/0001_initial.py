# Generated by Django 3.2.16 on 2022-11-02 07:46

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jon",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("thumbnail", models.ImageField(upload_to="images")),
                ("description", ckeditor.fields.RichTextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Apply",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254)),
                ("first_name", models.CharField(max_length=125)),
                ("last_name", models.CharField(max_length=125)),
                ("description", models.TextField(max_length=500)),
                ("resume", models.FileField(upload_to="file/")),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="job.jon"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
