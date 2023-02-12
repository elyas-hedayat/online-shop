from ckeditor.fields import RichTextField
from django.db import models

from utilities.models import SingletonModel


class ConfigBase(SingletonModel):
    image = models.ImageField(upload_to="images/")
    description = RichTextField(verbose_name="توضیحات")

    class Meta:
        abstract = True


class AboutUs(ConfigBase):
    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "دربازه ما"

    def __str__(self):
        return "درباره ما"


class Rule(ConfigBase):
    class Meta:
        verbose_name = "قوانین"
        verbose_name_plural = "قوانین"

    def __str__(self):
        return "قوانین"


class StoreRegistration(ConfigBase):
    class Meta:
        verbose_name = "شرایط ثبت فروشگاه"
        verbose_name_plural = "شرایط ثبت فروشگاه"

    def __str__(self):
        return "شرایط ثبت فروشگاه"


class CreditPurchase(ConfigBase):
    class Meta:
        verbose_name = "شرایط خرید اعتباری"
        verbose_name_plural = "شرایط خرید اعتباری"

    def __str__(self):
        return "شرایط خرید اعتباری"


class OrderPlacing(ConfigBase):
    class Meta:
        verbose_name = "مراحل ثبت سفارش"
        verbose_name_plural = "مراحل ثبت سفارش"

    def __str__(self):
        return "مراحل ثبت سفارش"


class Slider(models.Model):
    image = models.ImageField(verbose_name="اسلایدر", upload_to="sliders/")

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"

    def __str__(self):
        return f" اسلایدر شماره {self.id}"


class ContactUs(SingletonModel):
    phone = models.CharField("شماره تلفن", max_length=11)
    phone2 = models.CharField("شماره تلفن 2", max_length=11)
    phone3 = models.CharField("شماره تلفن 3", max_length=11)
    email = models.EmailField("ایمیل", max_length=254)
    explanation = RichTextField(verbose_name="توضیحات")
    address = RichTextField("آدرس", default="", max_length=1000)

    class Meta:
        verbose_name_plural = "تماس با ما"
        verbose_name = "تماس با ما"
