from rest_framework import serializers

from .models import AboutUs, ContactUs, CreditPurchase, OrderPlacing, Rule, Slider


class CreditPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditPurchase
        fields = (
            "image",
            "description",
        )


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            "image",
            "description",
        )


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            "image",
            "description",
        )


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = (
            "image",
            "description",
        )


class OrderPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPlacing
        fields = (
            "image",
            "description",
        )


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ("image",)


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            "phone",
            "phone2",
            "phone3",
            "email",
            "explanation",
            "address",
        )
