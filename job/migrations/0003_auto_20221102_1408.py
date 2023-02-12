# Generated by Django 3.2.16 on 2022-11-02 10:38

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0002_auto_20221102_1126"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "آگهی شغلی",
                "verbose_name_plural": "اگهایی شغلی",
            },
        ),
        migrations.AlterModelOptions(
            name="apply",
            options={"verbose_name": "درخواست", "verbose_name_plural": "درخواست ها"},
        ),
        migrations.AlterField(
            model_name="apply",
            name="job",
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to="job.job"
            ),
        ),
        migrations.DeleteModel(
            name="Jon",
        ),
    ]
