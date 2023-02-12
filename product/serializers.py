from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from category.serializers import CategorySerializer
from shop.serializers import ShopMainSerializer

from .models import Product, ProductImage, Promotion


class UploadedBase64ProductImageSerializer(serializers.Serializer):
    image = Base64ImageField(required=False)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "image", "product")


class ProductMainSerializer(serializers.ModelSerializer):
    shop = ShopMainSerializer()
    category = CategorySerializer()
    discount_id = serializers.SerializerMethodField()
    shop_name = serializers.CharField(source="shop.name")

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "category",
            "thumbnails",
            "shop",
            "price",
            "credit_sale",
            "inventory",
            "send_to_all_point",
            "price_with_offer",
            "discount_id",
            "shop_name",
        )

    def get_discount_id(self, obj):
        promotion_id = Promotion.objects.filter(product_id=obj.id)
        if promotion_id.exists():
            return promotion_id.values_list('id', flat=True)
        return None


class ProductCreateSerializer(serializers.ModelSerializer):
    image = UploadedBase64ProductImageSerializer(many=True, write_only=True)

    class Meta:
        model = Product
        fields = (
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
            "image",
            "inventory",
            "send_to_all_point",
        )

    def create(self, validated_data):
        images = validated_data.pop("image")
        image_list = []
        product_obj = Product.objects.create(**validated_data)
        for image_obj in images:
            image_list.append(ProductImage(product=product_obj, **image_obj))
        ProductImage.objects.bulk_create(image_list)
        return product_obj


class ProductDetailSerializer(ProductMainSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = ProductMainSerializer.Meta.model
        fields = ProductMainSerializer.Meta.fields + (
            "description",
            "feature",
            "images",
            "delivery_cost",
            "delivery_time",
            "transition",
        )

    def get_images(self, obj):
        return ImageSerializer(obj.images.all(), many=True).data


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = (
            "id",
            "product",
            "discount_amount",
        )

    def validate(self, data):
        if data["discount_amount"] >= data["product"].price:
            raise serializers.ValidationError(
                "discount must be less than product price"
            )
        return data
