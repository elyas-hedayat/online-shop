# Generated by Django 3.2.16 on 2022-12-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comment", "0014_auto_20221202_0251"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-posted"],
                "verbose_name": "کامنت",
                "verbose_name_plural": "کامنت ها",
            },
        ),
        migrations.AddField(
            model_name="comment",
            name="accepted",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(verbose_name="متن"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="ایمیل یا نام"
            ),
        ),
    ]