# Generated by Django 3.2.16 on 2022-11-20 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0004_auto_20221108_1253"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apply",
            name="phone_number",
            field=models.CharField(
                max_length=11,
                validators=[
                    django.core.validators.RegexValidator(
                        message="unvalid phonenumber", regex="^(\\+98|0)?9\\d{9}$"
                    )
                ],
                verbose_name="شماره تماس",
            ),
        ),
    ]
