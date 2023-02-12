# Generated by Django 3.2.16 on 2022-11-08 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import utilities.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ticket", "0003_alter_ticket_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="file",
            field=models.FileField(upload_to="files/", verbose_name="فایل"),
        ),
        migrations.AlterField(
            model_name="document",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="documents",
                to="ticket.message",
                verbose_name="پیام",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="message",
            field=models.TextField(verbose_name="پیام"),
        ),
        migrations.AlterField(
            model_name="message",
            name="ticket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="ticket.ticket",
                verbose_name="تیکت",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="priority",
            field=models.CharField(
                choices=[("high", "زیاد"), ("medium", "متوسط"), ("low", "کم")],
                max_length=15,
                verbose_name="درجه اهمیت",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="status",
            field=models.CharField(
                choices=[
                    ("unread", "خوانده نشده"),
                    ("closed", "بسته شده"),
                    ("pending", "در حال بررسی"),
                ],
                max_length=15,
                verbose_name="وضعیت",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="ticket_number",
            field=models.CharField(
                default=utilities.utils.create_random_number,
                max_length=6,
                verbose_name="شماره تیکت",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="title",
            field=models.CharField(max_length=125, verbose_name="عنوان"),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
    ]
