# Generated by Django 3.2.16 on 2022-11-02 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0007_r"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AdvertisingBanner",
        ),
        migrations.DeleteModel(
            name="NoticeBanner",
        ),
        migrations.DeleteModel(
            name="r",
        ),
    ]
