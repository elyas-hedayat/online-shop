# Generated by Django 3.2.16 on 2022-11-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("advertise", "0005_auto_20221102_1602"),
    ]

    operations = [
        migrations.AddField(
            model_name="advertisingbanner",
            name="first_row_first_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="first_row_fourth_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="first_row_second_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="first_row_third_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="second_row_first_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="second_row_fourth_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="second_row_second_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="second_row_third_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="third_row_first_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="third_row_fourth_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="third_row_second_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="advertisingbanner",
            name="third_row_third_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
    ]
