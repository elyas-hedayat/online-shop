from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from comment.models import Comment
from utilities.models import TimeStampModel
from utilities.validators import validate_file_size

user = settings.AUTH_USER_MODEL


class ActiveManager(models.Manager):
    """
    custom manager for getting just active shop
    """

    def active(self):
        return self.filter(is_active=True)


class Shop(TimeStampModel):
    user = models.OneToOneField(
        user,
        on_delete=models.CASCADE,
        related_name="shop",
        verbose_name="مالک",
    )
    name = models.CharField(
        unique=True,
        max_length=125,
        verbose_name="نام فروشگاه",
    )
    economic_code = models.CharField(
        max_length=30,
        verbose_name="شناسه ملی/کد ملی",
    )
    registration_number = models.CharField(
        max_length=30,
        verbose_name="شماره ثبت",
    )
    logo = models.ImageField(
        upload_to="shop/logo",
        verbose_name="لوگو",
    )
    state = models.CharField(
        max_length=125,
        verbose_name="استان",
    )
    city = models.CharField(
        max_length=125,
        verbose_name="شهر",
    )
    sheba_no = models.CharField(
        max_length=16,
        verbose_name="شماره شبا",
    )
    license_image = models.ImageField(
        upload_to="shop/images/",
        validators=[validate_file_size],
        verbose_name="عکس پروانه کسب",
    )
    national_card_image = models.ImageField(
        upload_to="shop/national_card/",
        validators=[validate_file_size],
        verbose_name="عکس کارت ملی",
    )
    suggestion = models.BooleanField(
        default=False,
        verbose_name="پیشنهاد پلاست اپ؟",
    )
    newest_shop = models.BooleanField(
        default=False,
        verbose_name="نمایش به عنوان جدیدترین فروشگاه؟",
    )
    most_popular = models.BooleanField(
        default=False,
        verbose_name="نمایش به عنوان محبوب ترین؟",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="فعال؟",
    )
    comments = GenericRelation(Comment)

    objects = ActiveManager()

    class Meta:
        verbose_name = "فروشگاه"
        verbose_name_plural = "فروشگاه ها"

    def __str__(self):
        return self.name

    @property
    def owner_full_name(self):
        return self.first_name + self.last_name
