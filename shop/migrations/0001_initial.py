# Generated by Django 3.2.16 on 2022-11-14 09:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import utilities.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Shop",
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
                ("name", models.CharField(max_length=125, unique=True)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "license_code",
                    models.CharField(max_length=30, verbose_name="کدآیسیک پروانه کسب"),
                ),
                (
                    "economic_code",
                    models.CharField(max_length=30, verbose_name="شناسه ملی/کد ملی"),
                ),
                (
                    "registration_number",
                    models.CharField(max_length=30, verbose_name="شماره ثبت"),
                ),
                ("logo", models.ImageField(upload_to="")),
                (
                    "most_popular",
                    models.BooleanField(
                        default=False, verbose_name="نمایش به عنوان محبوب ترین"
                    ),
                ),
                ("state", models.CharField(max_length=125)),
                ("city", models.CharField(max_length=125)),
                (
                    "image_license",
                    models.ImageField(
                        upload_to="shop/images/",
                        validators=[utilities.validators.validate_file_size],
                        verbose_name="عکس پروانه کسب",
                    ),
                ),
                (
                    "image_national_card",
                    models.ImageField(
                        upload_to="shop/national_card/",
                        validators=[utilities.validators.validate_file_size],
                        verbose_name="عکس کارت ملی",
                    ),
                ),
                (
                    "suggestion",
                    models.BooleanField(default=False, verbose_name="پیشنهاد پلاست اپ"),
                ),
                (
                    "newest_shop",
                    models.BooleanField(
                        default=False, verbose_name="نمایش به عنوان جدیدترین فروشگاه"
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
            options={
                "abstract": False,
            },
        ),
    ]
