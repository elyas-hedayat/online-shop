from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    logo = models.ImageField(upload_to="logo/", verbose_name="تصویر")
    title = models.CharField(max_length=125, verbose_name="عنوان")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class Commission(models.Model):
    percent = models.PositiveIntegerField(
        verbose_name="درصد کمیسیون", validators=[MaxValueValidator(100)]
    )
    category = models.OneToOneField(
        Category, on_delete=models.CASCADE, verbose_name="دسته بندی"
    )

    class Meta:
        unique_together = ["percent", "category"]
        verbose_name = "کمیسیون"
        verbose_name_plural = "کمیسیون ها"

    def __str__(self):
        return f"{self.percent} % برای دسته ی{self.category}"
