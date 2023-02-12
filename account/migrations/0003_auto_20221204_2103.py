# Generated by Django 3.2.16 on 2022-12-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_auto_20221108_1218"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=125, null=True, verbose_name="نام "
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=125, null=True, verbose_name="نام خانوادگی"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="profile/images"),
        ),
    ]