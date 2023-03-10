# Generated by Django 3.2.16 on 2022-11-15 08:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0003_auto_20221115_1147"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="most_popular",
            field=models.BooleanField(
                default=False, verbose_name="نمایش به عنوان محبوب ترین؟"
            ),
        ),
        migrations.AlterField(
            model_name="shop",
            name="newest_shop",
            field=models.BooleanField(
                default=False, verbose_name="نمایش به عنوان جدیدترین فروشگاه؟"
            ),
        ),
        migrations.AlterField(
            model_name="shop",
            name="suggestion",
            field=models.BooleanField(default=False, verbose_name="پیشنهاد پلاست اپ؟"),
        ),
        migrations.AlterField(
            model_name="shop",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
