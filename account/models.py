from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from utilities.validators import phone_number_regex

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    custom user model ;authentication with phone_number and password
    with
    3 different kind of accessibility
    """

    class Status(models.TextChoices):
        admin = "admin", "ادمین"
        business = "business", "تجاری"
        client = "client", "مشتری"

    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            phone_number_regex,
        ],
        verbose_name="شماره تلفن",
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default="client",
        verbose_name="نوع کاربر",
    )
    first_name = models.CharField(
        max_length=125, verbose_name="نام ", null=True, blank=True
    )
    last_name = models.CharField(
        max_length=125, verbose_name="نام خانوادگی", null=True, blank=True
    )
    thumbnail = models.ImageField(upload_to="profile/images", null=True, blank=True)
    user_point = models.PositiveIntegerField(verbose_name="امتیاز کاربر",default=0)

    is_admin = models.BooleanField(
        default=False,
        verbose_name="ادمین",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin

    def user_wallet(self):
        return 0

    user_wallet.short_description = "کیف پول کاربر"
