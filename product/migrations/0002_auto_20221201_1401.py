# Generated by Django 3.2.16 on 2022-12-01 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0003_alter_category_options"),
        ("shop", "0008_shop_sheba_no"),
        ("product", "0001_initial"),
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
                ("code", models.CharField(max_length=125)),
                ("required_point", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Promotion",
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
            ],
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "محصول", "verbose_name_plural": "محصولات"},
        ),
        migrations.AddField(
            model_name="product",
            name="amazing",
            field=models.BooleanField(default=False, verbose_name="شگفت انگیز"),
        ),
        migrations.AddField(
            model_name="product",
            name="best_seller",
            field=models.BooleanField(
                default=False, verbose_name="نمایش به عنوان بیشترین فروش"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="delivery_cost",
            field=models.IntegerField(default=1, verbose_name="هزینه ارسال"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="delivery_time",
            field=models.IntegerField(default=1, verbose_name="زمان ارسال(روز)"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="product",
            name="sales_unit",
            field=models.CharField(
                choices=[
                    ("box", "جعبه"),
                    ("roll", "رولی"),
                    ("pocket", "بسته\u200cای"),
                    ("numerical", "عددی"),
                    ("tom", "تن"),
                    ("kg", "کیلوگرم"),
                    ("g", "گرم"),
                ],
                default=1,
                max_length=200,
                verbose_name="واحد فروش",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="suggestion",
            field=models.BooleanField(default=False, verbose_name="پیشنهاد پلاست اپ"),
        ),
        migrations.AddField(
            model_name="product",
            name="thumbnails",
            field=models.ImageField(
                default=1, upload_to="product/thumbnail/", verbose_name="تصویر"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="transition",
            field=models.TextField(
                default=1, max_length=250, verbose_name="شرایط ارسال"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="category.category",
                verbose_name="دسته بندی",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="توضیحات"),
        ),
        migrations.AlterField(
            model_name="product",
            name="feature",
            field=models.JSONField(verbose_name="مشخصات"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(verbose_name="قیمت"),
        ),
        migrations.AlterField(
            model_name="product",
            name="shop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.shop",
                verbose_name="فروشگاه",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("accepted", "تایید شده"),
                    ("rejected", "رد شده"),
                    ("wait", "در حال بررسی"),
                ],
                max_length=12,
                verbose_name="وضعیت",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=125, verbose_name="عنوان"),
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        upload_to="product/images/", verbose_name="تصویر"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="product.product",
                        verbose_name="مصحول",
                    ),
                ),
            ],
            options={
                "verbose_name": "تصویر",
                "verbose_name_plural": "تصاویر",
            },
        ),
    ]
