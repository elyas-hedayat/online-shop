from django.db import models

from utilities.models import SingletonModel


class AdvertisingBanner(SingletonModel):
    """
    model for handling adv images
    """

    first_row_first_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف اول عکس اول"
    )
    first_row_first_url = models.URLField(
        verbose_name="آدزس",
    )

    first_row_second_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف اول عکس دوم"
    )
    first_row_second_url = models.URLField(
        verbose_name="آدزس",
    )

    first_row_third_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف اول عگس سوم "
    )
    first_row_third_url = models.URLField(
        verbose_name="آدزس",
    )

    first_row_fourth_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف اول عکس چهارم"
    )
    first_row_fourth_url = models.URLField(
        verbose_name="آدزس",
    )

    second_row_first_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف دوم عکس اول"
    )
    second_row_first_url = models.URLField(
        verbose_name="آدزس",
    )

    second_row_second_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف دوم عکس دوم"
    )
    second_row_second_url = models.URLField(
        verbose_name="آدزس",
    )

    second_row_third_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف دوم عکس سوم"
    )
    second_row_third_url = models.URLField(
        verbose_name="آدزس",
    )

    second_row_fourth_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف دوم عکس چهارم"
    )
    second_row_fourth_url = models.URLField(
        verbose_name="آدزس",
    )

    third_row_first_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف سوم عکس اول"
    )
    third_row_first_url = models.URLField(
        verbose_name="آدزس",
    )

    third_row_second_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف سوم عکس دوم "
    )
    third_row_second_url = models.URLField(
        verbose_name="آدزس",
    )

    third_row_third_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف سوم عکس سوم"
    )
    third_row_third_url = models.URLField(
        verbose_name="آدزس",
    )

    third_row_fourth_image = models.ImageField(
        upload_to="images/suggestion/", verbose_name="ردیف سوم عکس چهارم"
    )
    third_row_fourth_url = models.URLField(
        verbose_name="آدزس",
    )

    class Meta:
        verbose_name = "بنر تبلیغاتی"
        verbose_name_plural = "بنرهای تبلیغاتی"

    def __str__(self):
        return "بنر تبلیغاتی"


class NoticeBanner(SingletonModel):
    """
    models for showing  notif banner in plastapp platform
    """

    header_banner = models.ImageField(
        upload_to="banner/",
        verbose_name="بنر هدر",
    )
    header_banner_mobile = models.ImageField(
        upload_to="banner/",
        verbose_name="بنر هدر سایز موبایل",
    )
    header_banner_url = models.URLField(
        verbose_name="لینک بنر هدر",
    )

    first_row_first = models.ImageField(
        upload_to="banner/",
        verbose_name="ردیف اول عکس اول",
    )
    first_row_first_url = models.URLField(
        verbose_name="ردیف اول لینک اول",
    )
    first_row_second = models.ImageField(
        upload_to="banner/",
        verbose_name="ردیف اول عکس دوم",
    )
    first_row_second_url = models.URLField(
        verbose_name="ردیف اول لینک دوم",
    )

    second_row_first = models.ImageField(
        upload_to="banner/",
        verbose_name="ردیف دوم عکس اول",
    )
    second_row_first_url = models.URLField(
        verbose_name="ردیف دوم لینک اول",
    )
    second_row_second = models.ImageField(
        upload_to="banner/",
        verbose_name="ردیف دوم عکس دوم",
    )
    second_row_second_url = models.URLField(
        verbose_name="ردیف دوم لینک دوم",
    )

    class Meta:
        verbose_name = "بنر اطالع رسانی"
        verbose_name_plural = "بنرهای اطلاع رسانی"

    def __str__(self):
        return "بنر اطلاع رسانی"


class PartialData(SingletonModel):
    special_suggestion_text = models.CharField(
        max_length=255, verbose_name="متن محصولات ویژه"
    )
    special_suggestion_image = models.ImageField(
        upload_to="partial/", verbose_name=" عکس  محصولات ویژه"
    )
    best_seller_text = models.CharField(
        max_length=255, verbose_name="متن محولات پرفروش"
    )
    best_seller_image = models.ImageField(
        upload_to="partial/", verbose_name="متن محولات پرفروش"
    )
    product_text = models.CharField(max_length=255, verbose_name="متن محصولات")
    product_image = models.ImageField(
        upload_to="partial/", verbose_name=" عکس  محصولات"
    )
    mid_banner_text = models.CharField(max_length=255, verbose_name="متن شگفتانه")
    mid_banner_image = models.ImageField(
        upload_to="partial/", verbose_name="عکس شگفتانه"
    )

    def __str__(self):
        return "ایتم های صفحه اول"

    class Meta:
        verbose_name = "ایتم صفحه  اول"
        verbose_name_plural = "ایتم های صفحه اول"


class CustomerClub(models.Model):
    title = models.CharField(
        verbose_name="عنوان", max_length=255, blank=True, null=True
    )
    description = models.TextField(verbose_name="توضیحات")
    minimum_card_amount = models.IntegerField("حداقل سبد خرید", default=0)
    discount_rate = models.IntegerField("تخفیف", default=0)
    expired_after_day = models.IntegerField("انقضا پس از ... روز", default=0)
    needed_point = models.IntegerField("امتیاز مورد نیاز")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "کارت تخفیف"
        verbose_name_plural = "کارت های تخفیف"


class PointAfterBuy(models.Model):
    from_amount = models.IntegerField("از قیمت", default=0)
    to_amount = models.IntegerField("تا قیمت", default=0)
    prize_point = models.IntegerField("امتیاز جایزه")

    class Meta:
        verbose_name = "امتیاز پس از خرید"
        verbose_name_plural = "امتیاز پس از خرید"
