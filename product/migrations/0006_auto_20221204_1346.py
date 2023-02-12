# Generated by Django 3.2.16 on 2022-12-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_auto_20221202_0238"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="inventory",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="send_to_all_point",
            field=models.BooleanField(default=False),
        ),
    ]