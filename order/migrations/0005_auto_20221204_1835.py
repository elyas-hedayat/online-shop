# Generated by Django 3.2.16 on 2022-12-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0004_auto_20221204_1824"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coupon",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="coupon",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="coupon",
            name="coupon_token",
            field=models.CharField(max_length=255, verbose_name="کد تخفیف"),
        ),
    ]
