# Generated by Django 3.2.16 on 2022-11-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("advertise", "0003_remove_noticebanner_header_banner_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="noticebanner",
            name="header_banner_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="noticebanner",
            name="row_one_first_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="noticebanner",
            name="row_one_second_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="noticebanner",
            name="row_second_first_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="noticebanner",
            name="row_second_second_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
    ]
