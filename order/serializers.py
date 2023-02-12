from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from cart.models import Cart, CartItem
from product.serializers import ProductDetailSerializer

from .models import Cheque, CustomerClub, Order, OrderItem

user = get_user_model()


class ChequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheque
        fields = (
            "submitter",
            "description",
            "status",
            "cheque_image",
            "national_image",
            "amount",
        )
        read_only_fields = (
            "submitter",
            "status",
        )


class CustomerClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerClub
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "unit_price", "quantity", "commission"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "placed_at", "payment_status", "items"]


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["payment_status"]


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    state = serializers.CharField(write_only=True)
    city = serializers.CharField(write_only=True)
    postal_code = serializers.CharField(write_only=True)
    address_text = serializers.CharField(write_only=True)
    receiver_name = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("No cart with the given ID was found.")
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError("The cart is empty.")
        return cart_id

    def validate(self, attrs):
        cart_id = attrs["cart_id"]
        cart_obj = Cart.objects.get(pk=cart_id)
        if all(cart_obj.items.values_list("product__send_to_all_point")):
            return attrs
        else:
            for obj in cart_obj.items.all().select_related('product'):
                if (
                        not obj.shop.state == attrs['state']
                        and obj.product.send_to_all_point == False
                ):
                    raise serializers.ValidationError(
                        'all product"s shop must be in your state'
                    )
                return attrs

    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data["cart_id"]
            customer = user.objects.get(id=self.context["user_id"])
            order = Order.objects.create(
                customer=customer,
                state=self.validated_data["state"],
                city=self.validated_data["city"],
                postal_code=self.validated_data["postal_code"],
                address_text=self.validated_data["address_text"],
                receiver_name=self.validated_data["receiver_name"],
                phone_number=self.validated_data["phone_number"],
            )
            cart_items = CartItem.objects.select_related("product").filter(
                cart_id=cart_id
            )
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    unit_price=item.product.price,
                    quantity=item.quantity,
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(pk=cart_id).delete()
            return order


class DiscountCodeSerializer(serializers.Serializer):
    code = serializers.CharField(allow_null=True, allow_blank=True)
