# Generated by Django 3.2.16 on 2022-12-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comment", "0015_auto_20221202_0256"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="accepted",
            field=models.BooleanField(default=False, verbose_name="نمایش ؟"),
        ),
    ]
