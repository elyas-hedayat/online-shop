from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import strip_tags

from utilities.models import TimeStampModel

user = get_user_model()


class Blog(TimeStampModel):
    title = models.CharField(verbose_name="عنوان", max_length=255)
    author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        related_name="posts",
        limit_choices_to={"status": "admin"},
        verbose_name="نویسنده",
    )
    description = RichTextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images/", verbose_name="تصویر زمینه")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"

    def __str__(self):
        return self.title

    def estimate_reading_time(self):
        total = len(strip_tags(self.description).replace("&nbsp;", "").split())
        return total // 230
