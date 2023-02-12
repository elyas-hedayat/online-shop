from ckeditor.fields import RichTextField
from django.db import models

from utilities.models import TimeStampModel
from utilities.validators import phone_number_regex


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class Job(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name="عتوان شغلی")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر")
    description = RichTextField(verbose_name="توضیحات")
    active = models.BooleanField(default=True, verbose_name="فعال؟")

    objects = ActiveManager()

    class Meta:
        verbose_name = "آگهی شغلی"
        verbose_name_plural = "اگهایی شغلی"

    def __str__(self):
        return self.title


class Apply(TimeStampModel):
    email = models.EmailField(
        verbose_name="ایمیل",
    )
    first_name = models.CharField(
        max_length=125,
        verbose_name=" نام",
    )
    last_name = models.CharField(
        max_length=125,
        verbose_name="نام خانوادگی",
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="شماره تماس",
        validators=[phone_number_regex],
    )
    description = models.TextField(
        max_length=500,
        verbose_name="توضیحات",
    )
    resume = models.FileField(
        upload_to="file/",
        verbose_name="رزومه",
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        verbose_name="آگهی شغلی",
    )

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست ها"

    def __str__(self):
        return f"{self.first_name}-{self.last_name} درخواست برای {self.job.title}"
