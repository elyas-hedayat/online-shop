from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from category.models import Category
from comment.models import Comment
from shop.models import Shop
from utilities.models import TimeStampModel


class ActiveProductManager(models.Manager):
    def active(self):
        return self.filter(status="accepted", is_active=True)


class Promotion(models.Model):
    product = models.OneToOneField(
        "Product",
        on_delete=models.CASCADE,
        related_name="discount",
        verbose_name="مصحصول",
    )
    discount_amount = models.PositiveIntegerField(verbose_name="مقدار تخقیف")

    class Meta:
        verbose_name = "تخقیف"
        verbose_name_plural = "تخفیفات"


class Product(TimeStampModel):
    """
    super_user will specifies following field
    (means that their value won't  calculate automatically):
    status,suggestion,amazing,best_seller

    after obj status change to accept that obj will display in site

    """

    class STATUS(models.TextChoices):
        accept = "accepted", "تایید شده"
        reject = "rejected", "رد شده"
        wait = "wait", "در حال بررسی"

    class SALSE_UNIT(models.TextChoices):
        box = "box", "جعبه"
        roll = "roll", "رولی"
        packet = "pocket", "بسته‌ای"
        numerical = "numerical", "عددی"
        ton = "tom", "تن"
        kg = "kg", "کیلوگرم"
        g = "g", "گرم"

    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        verbose_name="فروشگاه",
    )
    title = models.CharField(
        max_length=125,
        verbose_name="عنوان",
    )
    description = models.TextField(
        verbose_name="توضیحات",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="دسته بندی",
    )
    feature = models.JSONField(
        verbose_name="مشخصات",
    )
    status = models.CharField(
        verbose_name="وضعیت",
        max_length=12,
        choices=STATUS.choices,
    )
    price = models.PositiveIntegerField(
        verbose_name="قیمت",
    )
    thumbnails = models.ImageField(
        verbose_name="تصویر",
        upload_to="product/thumbnail/",
    )
    sales_unit = models.CharField(
        choices=SALSE_UNIT.choices,
        max_length=200,
        verbose_name="واحد فروش",
    )
    delivery_cost = models.IntegerField(
        verbose_name="هزینه ارسال",
    )
    delivery_time = models.IntegerField(
        verbose_name="زمان ارسال(روز)",
    )

    transition = models.TextField(
        max_length=250,
        verbose_name="شرایط ارسال",
    )
    inventory = models.PositiveIntegerField()
    send_to_all_point = models.BooleanField(default=False)

    credit_sale = models.BooleanField(
        verbose_name="فروش اعتباری",
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    suggestion = models.BooleanField(
        verbose_name="پیشنهاد پلاست اپ",
        default=False,
    )
    amazing = models.BooleanField(
        verbose_name="شگفت انگیز",
        default=False,
    )
    best_seller = models.BooleanField(
        verbose_name="نمایش به عنوان بیشترین فروش",
        default=False,
    )
    comments = GenericRelation(Comment)

    objects = ActiveProductManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    def remove_items_from_inventory(self, count=1, save=True):
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory

    @property
    def price_with_offer(self):
        if self.discount:
            return self.price - self.discount.discount_amount
        return self.price


class ProductImage(TimeStampModel):
    image = models.ImageField(verbose_name="تصویر", upload_to="product/images/")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="مصحول"
    )

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"
