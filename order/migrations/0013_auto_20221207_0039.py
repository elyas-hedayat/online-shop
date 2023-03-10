# Generated by Django 3.2.16 on 2022-12-06 21:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0006_auto_20221204_1346"),
        ("order", "0012_auto_20221207_0003"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="مشتری",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_status",
            field=models.CharField(
                choices=[("P", "Pending"), ("C", "Complete"), ("F", "Failed")],
                default="P",
                max_length=1,
                verbose_name="وضعیت پرداخت",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="placed_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="ثبت شده در تاریخ"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="commission",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="کمیسیون"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orderitems",
                to="product.product",
                verbose_name="محصول",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.PositiveSmallIntegerField(verbose_name="مقدار"),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="unit_price",
            field=models.PositiveSmallIntegerField(verbose_name="قیمت هر واحد"),
        ),
    ]
