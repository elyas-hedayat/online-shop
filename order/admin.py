from django.contrib import admin
from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Cheque, Coupon, CustomerClub, Order, OrderItem, PrizeOfBuy


class CouponAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["user", "get_expired_jalali", "coupon_token"]

    def get_expired_jalali(self, obj):
        for_show = date2jalali(obj.expired_date)
        return for_show.strftime("%Y/%m/%d") if for_show else ""

    get_expired_jalali.short_description = "تاریخ انقضا"
    get_expired_jalali.admin_order_field = "اعتبار"


class ChequeAdmin(admin.ModelAdmin):
    readonly_fields = (
        "submitter",
        "description",
        "cheque_image",
        "national_image",
        "amount",
    )


admin.site.register(Cheque, ChequeAdmin)

admin.site.register(Coupon, CouponAdmin)
admin.site.register(CustomerClub)
admin.site.register(PrizeOfBuy)


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemTabularInline,
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
