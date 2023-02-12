# Generated by Django 3.2.16 on 2022-12-04 14:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0003_customerclub"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrizeOfBuy",
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
                ("form_amount", models.IntegerField(verbose_name="از (تومان)")),
                ("to_amount", models.IntegerField(verbose_name="تا (تومان)")),
                ("point", models.IntegerField(verbose_name="امتیاز")),
            ],
            options={
                "verbose_name": "کد تخفیف اتوماتیک",
                "verbose_name_plural": "کدهای تخفیف اتوماتیک",
            },
        ),
        migrations.AddField(
            model_name="coupon",
            name="user",
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL, verbose_name="کاربر"
            ),
        ),
    ]