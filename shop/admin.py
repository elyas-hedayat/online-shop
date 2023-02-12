from django.contrib import admin
from django.utils.html import format_html

from .forms import ShopChangeForm
from .models import Shop


@admin.register(Shop)
class ShopAdminModel(admin.ModelAdmin):
    form = ShopChangeForm
    list_display = (
        "user",
        "name",
        "shop_logo",
        "is_active",
    )
    search_fields = ("name",)
    list_filter = (
        "is_active",
        "most_popular",
        "newest_shop",
        "suggestion",
    )
    readonly_fields = (
        "user",
        "shop_logo",
        "national_card_image_preview",
        "license_image_preview",
        "name",
        "economic_code",
        "registration_number",
        "sheba_no",
    )
    fieldsets = (
        (
            "اطلاعات مالک",
            {
                "fields": (
                    "user",
                    ("sheba_no",),
                )
            },
        ),
        (
            "اطلاعات فروشگاه",
            {
                "classes": (
                    "wide",
                    "extrapretty",
                ),
                "fields": (
                    "name",
                    (
                        "economic_code",
                        "registration_number",
                        "state",
                        "city",
                    ),
                ),
            },
        ),
        (
            "تصاویر",
            {
                "classes": (
                    "wide",
                    "extrapretty",
                ),
                "fields": (
                    "shop_logo",
                    (
                        "national_card_image_preview",
                        "license_image_preview",
                    ),
                ),
            },
        ),
        (
            "ارتقا",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "suggestion",
                        "newest_shop",
                        "most_popular",
                    ),
                ),
            },
        ),
    )

    @admin.display(description="لوگوی فروشگاه")
    def shop_logo(self, obj):
        return format_html(
            '<a href="{}"><img  width="100px" height="100px" src={}></a>'.format(
                obj.logo.url,
                obj.logo.url,
            )
        )

    @admin.display(description=" کارت ملی")
    def national_card_image_preview(self, obj):
        return format_html(
            '<a href="{}"><img  width="200px" height="200px" src={}></a>'.format(
                obj.national_card_image.url,
                obj.national_card_image.url,
            )
        )

    @admin.display(description="پروانه کسب")
    def license_image_preview(self, obj):
        return format_html(
            '<a href="{}"><img  width="200px"  height="200px" src={}></a>'.format(
                obj.license_image.url,
                obj.license_image.url,
            )
        )

    def has_add_permission(self, request):
        return False
