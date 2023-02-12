from django.conf import settings
from django.db import models
from django.utils.html import format_html

from utilities.models import TimeStampModel
from utilities.utils import create_random_number

user = settings.AUTH_USER_MODEL


class Ticket(TimeStampModel):
    class STATUS(models.TextChoices):
        unread = "unread", "خوانده نشده"
        closed = "closed", "بسته شده"
        pending = "pending", "در حال بررسی"

    class PRIORITY(models.TextChoices):
        high = "high", "زیاد"
        medium = "medium", "متوسط"
        low = "low", "کم"

    title = models.CharField(max_length=125, verbose_name="عنوان")
    user = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name="tickets", verbose_name="کاربر"
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS.choices,
        verbose_name="وضعیت",
        default="unread",
    )
    priority = models.CharField(
        max_length=15, choices=PRIORITY.choices, verbose_name="درجه اهمیت"
    )
    ticket_number = models.CharField(
        max_length=6, default=create_random_number, verbose_name="شماره تیکت"
    )

    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"

    def __str__(self):
        return self.title


class Message(TimeStampModel):
    class SENDER(models.TextChoices):
        admin = "admin", "ادمین"
        customer = "customer", "مشتری"

    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="messages", verbose_name="تیکت"
    )
    message = models.TextField(verbose_name="پیام")
    sender = models.CharField(
        max_length=12,
        verbose_name="ارسال کننده",
        choices=SENDER.choices,
        default="customer",
    )

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return self.message[:50]

    def changeform_link(self):
        if self.id:
            changeform_url = (
                f"http://127.0.0.1:8000/admin/ticket/message/{self.id}/change/"
            )
            return format_html(
                '<a href="%s" target="_blank">Details</a>' % changeform_url
            )
        return ""

    changeform_link.allow_tags = True
    changeform_link.short_description = ""


class Document(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="documents", verbose_name="پیام"
    )
    file = models.FileField(upload_to="files/", verbose_name="فایل")

    class Meta:
        verbose_name = "فایل "
        verbose_name_plural = "فایل ها"
