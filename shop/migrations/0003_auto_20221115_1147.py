# Generated by Django 3.2.16 on 2022-11-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_auto_20221114_1357"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shop",
            name="license_code",
        ),
        migrations.AlterField(
            model_name="shop",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="فعال؟"),
        ),
    ]
