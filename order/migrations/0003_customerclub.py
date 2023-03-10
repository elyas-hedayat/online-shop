# Generated by Django 3.2.16 on 2022-12-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_coupon"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerClub",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="عنوان"
                    ),
                ),
                ("description", models.TextField(verbose_name="توضیحات")),
                (
                    "minimum_card_amount",
                    models.IntegerField(default=0, verbose_name="حداقل سبد خرید"),
                ),
                ("discount_rate", models.IntegerField(default=0, verbose_name="تخفیف")),
                ("needed_point", models.IntegerField(verbose_name="امتیاز مورد نیاز")),
            ],
            options={
                "verbose_name": "باشگاه مشتریان",
                "verbose_name_plural": "باشگاه مشتریان",
            },
        ),
    ]
