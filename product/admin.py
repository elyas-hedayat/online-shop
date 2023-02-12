from django.contrib import admin
from django.utils.html import format_html

from .models import Product, ProductImage, Promotion


admin.site.register(ProductImage)

class PromotionInline(admin.TabularInline):
    model = Promotion
    fields = ("discount_amount",)
    readonly_fields = ("discount_amount",)

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ("image_preview",)
    readonly_fields = ("image_preview",)

    @admin.display(description="تصویر")
    def image_preview(self, obj):
        return format_html(
            '<a href="{}"><img  width="100px" height="100px" src={}></a>'.format(
                obj.image.url,
                obj.image.url,
            )
        )

    def has_add_permission(self, request, obj):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.fields

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "اطلاعات محصول",
            {
                "fields": (
                    (
                        "thumbnail_preview",
                        "shop",
                        "status",
                    ),
                    ("title", "description"),
                    (
                        "feature",
                        "category",
                    ),
                )
            },
        ),
        (
            "شرایط ارسال",
            {
                "fields": (
                    "delivery_cost",
                    "delivery_time",
                    "transition",
                )
            },
        ),
        (
            "شرایط محصول",
            {
                "fields": (("is_active", "credit_sale"),),
            },
        ),
        (
            "ارتقا",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "suggestion",
                        "amazing",
                        "best_seller",
                    ),
                ),
            },
        ),
    )
    model = Product
    inlines = (ProductImageInline, PromotionInline)
    list_select_related = ["shop", "category"]
    list_filter = ("is_active", "suggestion", "amazing", "best_seller")
    search_fields = ("title",)
    list_per_page = 20
    list_display = ("title", "thumbnail_preview", "price", "status")
    readonly_fields = (
        "shop",
        "title",
        "description",
        "category",
        "feature",
        "price",
        "thumbnails",
        "sales_unit",
        "delivery_cost",
        "delivery_time",
        "transition",
        "credit_sale",
        "is_active",
        "thumbnail_preview",
    )

    @admin.display(description="تصویر")
    def thumbnail_preview(self, obj):
        return format_html(
            '<a href="{}"><img  width="100px" height="100px" src={}></a>'.format(
                obj.thumbnails.url,
                obj.thumbnails.url,
            )
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
