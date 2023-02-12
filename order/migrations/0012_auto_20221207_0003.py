# Generated by Django 3.2.16 on 2022-12-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0011_order_orderitem"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "permissions": [("cancel_order", "Can cancel order")],
                "verbose_name": "سفارش",
                "verbose_name_plural": "سفارشات",
            },
        ),
        migrations.AlterModelOptions(
            name="orderitem",
            options={"verbose_name": "محصول", "verbose_name_plural": "محصولات"},
        ),
        migrations.AddField(
            model_name="orderitem",
            name="commission",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]