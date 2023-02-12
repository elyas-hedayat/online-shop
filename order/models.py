from django.conf import settings
from django.db import models
from jalali_date import date2jalali

from category.models import Commission
from product.models import Product
from utilities.models import TimeStampModel
from utilities.utils import send_sms

user = settings.AUTH_USER_MODEL


class Coupon(TimeStampModel):
    coupon_token = models.CharField(verbose_name="کد تخفیف", max_length=255)
    minimum_card_amount = models.IntegerField(verbose_name="حداقل سبد خرید")
    discount_rate = models.IntegerField(verbose_name="تخفیف")
    user = models.ForeignKey(
        user,
        verbose_name="کاربر",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    expired_date = models.DateField(verbose_name="معتبر تا")

    def __str__(self):
        return "حداقل خرید: {} -  تخفیف:{}".format(
            self.minimum_card_amount, self.discount_rate
        )

    def save(self, *args, **kwargs):
        expired = date2jalali(self.expired_date).strftime("%Y/%m/%d")
        text = f"""کاربر عزیز پلاست‌اپی
    کد تخفیف: {self.coupon_token}
    حداقل خرید: {self.minimum_card_amount} تومان
    مبلغ تخفیف: {self.discount_rate} تومان
    اعتبار تا: {expired}
    برای شما فعال شد.
    پلاست‌اپ
    plastapp.ir"""
        try:
            send_sms(self.user.phone_number, "", text)
        except Exception as e:
            print(e)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "کوپن"
        verbose_name_plural = "کوپن ها"


class Cheque(TimeStampModel):
    class StatusOptions(models.TextChoices):
        PENDING = "P", "در حال بررسی"
        ACCEPTED = "A", "تایید شده"
        REJECTED = "R", "رد شده"

    submitter = models.ForeignKey(
        user,
        verbose_name="کاربر",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    description = models.TextField(verbose_name="توضیحات", blank=True, null=True)
    status = models.CharField(
        verbose_name="وضعیت",
        max_length=255,
        default=StatusOptions.PENDING,
        choices=StatusOptions.choices,
    )
    cheque_image = models.ImageField(
        verbose_name="عکس چک",
        upload_to="check/images/",
    )
    national_image = models.ImageField(
        verbose_name="عکس کارت ملیگ", upload_to="check/images/"
    )
    amount = models.IntegerField(verbose_name="مبلغ چک")
    used = models.BooleanField(default=False, verbose_name="استفاده شده>")

    # tracking_code = models.IntegerField()

    class Meta:
        verbose_name = "چک"
        verbose_name_plural = "چک ها"

    def save(self, *args, **kwargs):
        if self.status == self.StatusOptions.ACCEPTED:
            text = "وضعیت چک شما بررسی شد. خرید اعتباری برای شما امکان پذیر میباشد.\nپلاست‌اپ\nplastapp.ir"
        elif self.status == self.StatusOptions.REJECTED:
            text = "وضعیت چک شما بررسی شد.\nمتاسفانه امکان خرید اعتباری برای شما مقدور نمیباشد.\nجهت کسب اطلاعات بیشتر با پشتیبانی در ارتباط باشید.\nپلاست‌اپ\n02144101711"
        else:
            text = "وضعیت چک شما در حال بررسی است.\nنتیجه از طریق پیامک به شما اعلام میگردد.\nپلاست‌اپ\nplastapp.ir"

        try:
            send_sms(self.submitter.phone_number, "", text)
        except Exception as e:
            print(e)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.submitter.phone_number}"


class CustomerClub(models.Model):
    title = models.CharField(
        verbose_name="عنوان", max_length=255, blank=True, null=True
    )
    description = models.TextField(verbose_name="توضیحات")
    minimum_card_amount = models.IntegerField(verbose_name="حداقل سبد خرید", default=0)
    discount_rate = models.IntegerField(verbose_name="تخفیف", default=0)
    needed_point = models.IntegerField(verbose_name="امتیاز مورد نیاز")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "باشگاه مشتریان"
        verbose_name_plural = "باشگاه مشتریان"


class PrizeOfBuy(models.Model):
    form_amount = models.IntegerField(verbose_name="از (تومان)")
    to_amount = models.IntegerField(verbose_name="تا (تومان)")
    point = models.IntegerField(verbose_name="امتیاز")

    def __str__(self):
        return f"{self.form_amount} - {self.to_amount} - {self.point}"

    class Meta:
        verbose_name = "امتیاز خرید"
        verbose_name_plural = "امتباز خرید"


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]

    placed_at = models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در تاریخ")
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING,
        verbose_name="وضعیت پرداخت",
    )
    customer = models.ForeignKey(user, on_delete=models.PROTECT, verbose_name="مشتری")
    state = models.CharField(max_length=125, verbose_name="استان")
    city = models.CharField(max_length=125, verbose_name="شهر")
    postal_code = models.CharField(verbose_name="کد پستی", default="", max_length=20)
    address_text = models.TextField(verbose_name="آدرس", default="", max_length=250)
    receiver_name = models.CharField(verbose_name="نام گیرنده", max_length=255)
    phone_number = models.CharField(verbose_name="شماره تلفن", max_length=11)
    discount = models.PositiveIntegerField(verbose_name="مقدار تخفیف", default=0)
    payment_tracking_code = models.CharField(
        verbose_name="کد پیگری پرداخت", max_length=125
    )

    class Meta:
        permissions = [("cancel_order", "Can cancel order")]
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    @property
    def get_delivery_cost(self):
        total_delivery = sum(item.product.delivery_cost for item in self.items.all())
        return total_delivery

    def get_total_price(self):
        total = (
            sum(item.get_cost() for item in self.items.all()) + self.get_delivery_cost
        )
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="orderitems",
        verbose_name="محصول",
    )
    quantity = models.PositiveSmallIntegerField(verbose_name="مقدار")
    unit_price = models.PositiveSmallIntegerField(verbose_name="قیمت هر واحد")
    commission = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="کمیسیون"
    )

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def save(self, *args, **kwargs):
        product_category_commission = self.product.category.commission.percent
        total_price = self.unit_price * self.quantity
        self.commission = total_price // product_category_commission
        return super(OrderItem, self).save(*args, **kwargs)

    def get_cost(self):
        return self.unit_price * self.quantity
