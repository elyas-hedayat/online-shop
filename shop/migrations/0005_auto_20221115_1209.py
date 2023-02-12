# Generated by Django 3.2.16 on 2022-11-15 08:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0004_auto_20221115_1153"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="city",
            field=models.CharField(max_length=125, verbose_name="شهر"),
        ),
        migrations.AlterField(
            model_name="shop",
            name="logo",
            field=models.ImageField(upload_to="shop/logo", verbose_name="لوگو"),
        ),
        migrations.AlterField(
            model_name="shop",
            name="name",
            field=models.CharField(
                max_length=125, unique=True, verbose_name="نام فروشگاه"
            ),
        ),
        migrations.AlterField(
            model_name="shop",
            name="state",
            field=models.CharField(max_length=125, verbose_name="استان"),
        ),
        migrations.AlterField(
            model_name="shop",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop",
                to=settings.AUTH_USER_MODEL,
                verbose_name="مالک",
            ),
        ),
    ]