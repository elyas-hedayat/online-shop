from rest_framework import serializers

from .models import Shop


class ShopMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "user",
            "id",
            "name",
            "logo",
        )
        read_only_fields = ("user",)


class ShopSerializer(ShopMainSerializer):
    class Meta:
        model = ShopMainSerializer.Meta.model
        fields = ShopMainSerializer.Meta.fields + (
            "is_active",
            "economic_code",
            "registration_number",
            "most_popular",
            "state",
            "city",
            "license_image",
            "national_card_image",
            "suggestion",
            "newest_shop",
            "sheba_no",
        )
        read_only_fields = ("user",)
