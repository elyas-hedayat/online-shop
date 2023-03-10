# Generated by Django 3.2.16 on 2022-12-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0014_alter_coupon_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address_text",
            field=models.TextField(default="", max_length=250, verbose_name="آدرس"),
        ),
        migrations.AddField(
            model_name="order",
            name="city",
            field=models.CharField(default=1, max_length=125, verbose_name="شهر"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="phone_number",
            field=models.CharField(default=1, max_length=11, verbose_name="شماره تلفن"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="postal_code",
            field=models.CharField(default="", max_length=20, verbose_name="کد پستی"),
        ),
        migrations.AddField(
            model_name="order",
            name="receiver_name",
            field=models.CharField(
                default=1, max_length=255, verbose_name="نام گیرنده"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="state",
            field=models.CharField(default=1, max_length=125, verbose_name="استان"),
            preserve_default=False,
        ),
    ]
