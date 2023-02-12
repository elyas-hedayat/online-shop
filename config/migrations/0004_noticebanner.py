# Generated by Django 3.2.16 on 2022-11-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0003_alter_slider_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="NoticeBanner",
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
                ("header_banner", models.ImageField(upload_to="banner/")),
                ("header_banner_mobile", models.ImageField(upload_to="banner/")),
                ("row_one_first", models.ImageField(upload_to="banner/")),
                ("row_one_second", models.ImageField(upload_to="banner/")),
                ("row_second_first", models.ImageField(upload_to="banner/")),
                ("row_second_second", models.ImageField(upload_to="banner/")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]