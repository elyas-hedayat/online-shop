# Generated by Django 3.2.16 on 2022-12-02 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comment", "0013_auto_20221201_1348"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="email",
            field=models.EmailField(blank=True, max_length=254, verbose_name="ایمیل"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="comment.comment",
                verbose_name="کامنت اصلی",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
    ]
