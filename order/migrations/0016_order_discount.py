# Generated by Django 3.2.16 on 2022-12-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0015_auto_20221211_1210"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.PositiveIntegerField(default=0, verbose_name="مقدار تخفیف"),
        ),
    ]
