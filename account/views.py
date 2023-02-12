from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.core.cache import cache
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from utilities.utils import send_otp

from .serializers import (
    AuthSerializer,
    ChangePasswordSerializer,
    ForgetPasswordSerializer,
    LoginSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
    UserSerializer,
    VerifyCodeSerializer,
)

user = get_user_model()


class SendOtpApiView(generics.GenericAPIView):
    """
    post:
        send otp for user for registration;
        note:if user requested for code before must wait(
        If less than two minutes have passed
        )
    """

    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            send_otp(phone_number=serializer_data.validated_data["phone_number"])
            return Response(data={"message": "message sent"})
        return Response(data={"message": serializer_data.errors})


class VerifyUserRegistrationApiView(generics.GenericAPIView):
    """
    post:
        verify otp code that sent for registration
            if code match delete cache key  and set new cache as confirm
    """

    serializer_class = VerifyCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            phone_number = serializer_data.validated_data["phone_number"]
            cache.delete(f"{phone_number}-for-authentication")
            cache.set(phone_number, "confirm", 1000)
            return Response(data={"message": "account confirmed"})
        return Response(data=serializer_data.errors)


class UserRegisterApiView(generics.GenericAPIView):
    """
    post:
        register user if user phone_number keys stored in cache data as  confirm ,
        after registration user phone_number will delete from cache data;
        note:all the user registered as customer at first

    """

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            serializer_data.save()
            cache.delete(serializer_data.validated_data["phone_number"])
            return Response(data={"message": "user created"})
        return Response(data=serializer_data.errors)


class LoginApiView(generics.GenericAPIView):
    """
    post:
        user can login with phone_number and password
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            user_obj = authenticate(
                phone_number=serializer_data.validated_data["phone_number"],
                password=serializer_data.validated_data["password"],
            )
            print(user_obj)
            if user_obj:
                token = RefreshToken.for_user(user_obj)
                data = {
                    "refresh": str(token),
                    "access": str(token.access_token),
                }
                return Response(data=data)
            return Response(data={"message": "no user with this credential   exists "})
        return Response(data={"message": serializer_data.errors})


class ChangePasswordApiView(generics.GenericAPIView):
    """
    post:
        user can change their password with provided data
        note:validation on this endpoint:
            old password and new password must not be same;
            length of  new_password must value must  be in range(6,9)
            value that provided as old password must be same with user original password;
    """

    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            old_password = serializer_data.validated_data["old_password"]
            new_password = serializer_data.validated_data["new_password"]
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return Response(
                    data={"message": "password successfully changed"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                data={"message": "old password is wrong"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            data={"message": serializer_data.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(generics.GenericAPIView):
    """
    post:
        user access token will add to blacklist
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(data={"message": e}, status=status.HTTP_400_BAD_REQUEST)


class ForgetPasswordOtpSendApiView(generics.GenericAPIView):
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            send_otp(serializer_data.validated_data["phone_number"])
            return Response(data={"message": "code send"})
        return Response(data=serializer_data.errors)


class ForgetPasswordVerifyApiView(generics.GenericAPIView):
    """
    if user entered code equal to code that sent user
    account will confirm   for changing password
    """

    serializer_class = VerifyCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            phone_number = serializer_data.validated_data["phone_number"]
            cache.delete(f"{phone_number}-for-authentication")
            cache.set(phone_number, "confirm", settings.EXPIRY_TIME_OTP)
            return Response(data={"message": "account confirmed for changing password"})
        return Response(data=serializer_data.errors)


class ForgetPassword(generics.GenericAPIView):
    """
    user password will update in this api
    if data is valid
    """

    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            phone_number = serializer_data.validated_data["phone_number"]
            cache.delete(phone_number)
            user_obj = user.objects.get(phone_number=phone_number)
            user_obj.set_password(serializer_data.validated_data["password"])
            user_obj.save()
            return Response(data={"message": "password successfully reset"})
        return Response(data=serializer_data.errors)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        self.get_token(self.user)
        data["status"] = self.user.status
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserInfoApiView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.request.user).data)


class UserUpdateInfoApiView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self):
        return user.objects.get(id=self.request.user.id)
