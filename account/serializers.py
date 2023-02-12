from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import serializers
from rest_framework.validators import ValidationError

from utilities.validators import phone_number_regex

user = get_user_model()


class AuthSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_number_regex])

    def validate(self, data):
        phone_number = data["phone_number"]
        user_obj = user.objects.filter(phone_number=phone_number)
        if cache.get(f"{phone_number}-for-authentication"):
            raise serializers.ValidationError(detail="try later")
        elif user_obj.exists():
            raise serializers.ValidationError(detail="user already exist")
        return data


class ForgetPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_number_regex])

    def validate(self, data):
        phone_number = data["phone_number"]
        user_obj = user.objects.filter(phone_number=phone_number)
        if not user_obj.exists():
            raise serializers.ValidationError(
                detail="account's  with this phone_number dose not exists"
            )
        elif cache.get(f"{phone_number}-for-authentication"):
            raise serializers.ValidationError(detail="try later")
        return data


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        validators=[
            phone_number_regex,
        ]
    )
    password = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    old_password = serializers.CharField()

    def validate(self, data):
        if data["new_password"] == data["old_password"]:
            raise ValidationError("old and new password are same")
        if not 8 >= len(data["new_password"]) >= 6:
            raise serializers.ValidationError(
                detail="new password char must be in range 6 and 9"
            )
        return data


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()

    class Meta:
        model = user
        fields = ("phone_number", "password", "password_confirm")

    def validate(self, data):
        if not cache.get(data["phone_number"]):
            raise serializers.ValidationError(
                detail={"this phone_number not confirmed"}
            )
        if (
            not 8 >= len(data["password"]) >= 6
            or data["password"] != data["password_confirm"]
        ):
            raise serializers.ValidationError(
                detail="new password char must be in range 6 and 9"
            )
        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        return user.objects.create_user(**validated_data)


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()

    def validate(self, data):
        phone_number = data["phone_number"]
        get_phone_number = cache.get(f"{phone_number}-for-authentication")
        if not get_phone_number:
            raise serializers.ValidationError("code expired")
        elif str(get_phone_number) != data["code"]:
            raise serializers.ValidationError('code aren"t match')
        return data


class ResetPasswordSerializer(serializers.Serializer):
    password_confirm = serializers.CharField()
    phone_number = serializers.CharField()
    password = serializers.CharField()

    # class Meta:
    #     model = user
    #     fields = ("phone_number", "password", "password_confirm")

    def validate(self, data):
        user_obj = user.objects.get(phone_number=data["phone_number"])
        if not cache.get(data["phone_number"]):
            raise serializers.ValidationError(
                detail={"this phone_number not confirmed"}
            )
        if (
            not 8 >= len(data["password"]) >= 6
            or data["password"] != data["password_confirm"]
        ):
            raise serializers.ValidationError(
                detail="new password char must be in range 6 and 9"
            )
        if user_obj.check_password(data["password"]):
            raise serializers.ValidationError(
                "this password is same as your pld password"
            )
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = (
            "phone_number",
            "first_name",
            "last_name",
            "user_point",
            "user_wallet",
        )
        read_only_fields = (
            "phone_number",
            "user_point",
            "user_wallet",
        )
