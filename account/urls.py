from django.urls import path

from .views import (
    ChangePasswordApiView,
    ForgetPassword,
    ForgetPasswordOtpSendApiView,
    ForgetPasswordVerifyApiView,
    LoginApiView,
    LogoutView,
    MyTokenObtainPairView,
    SendOtpApiView,
    UserInfoApiView,
    UserRegisterApiView,
    UserUpdateInfoApiView,
    VerifyUserRegistrationApiView,
)

urlpatterns = [
    path("login/", LoginApiView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("change_password/", ChangePasswordApiView.as_view()),
    path("send_otp/", SendOtpApiView.as_view()),
    path("verify_register/", VerifyUserRegistrationApiView.as_view()),
    path("register/", UserRegisterApiView.as_view()),
    path("forget_password_send_otp/", ForgetPasswordOtpSendApiView.as_view()),
    path("forget_password_verify/", ForgetPasswordVerifyApiView.as_view()),
    path("forget_password/", ForgetPassword.as_view()),
    path("token/", MyTokenObtainPairView.as_view()),
    path("info/", UserInfoApiView.as_view()),
    path("update_info/", UserUpdateInfoApiView.as_view()),
]
