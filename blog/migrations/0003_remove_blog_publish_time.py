# Generated by Django 3.2.16 on 2022-11-14 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_publish_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="publish_time",
        ),
    ]
