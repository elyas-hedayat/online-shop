from django.urls import path

from .views import (
    AboutUsApiView,
    ContactUsApiView,
    CreditPurchaseApiView,
    OrderPlaceApiView,
    RuleApiView,
    SliderListApiView,
    StoreRegistrationApiView,
)

urlpatterns = [
    path("rule/", RuleApiView.as_view()),
    path("about_us/", AboutUsApiView.as_view()),
    path("slider/", SliderListApiView.as_view()),
    path("contact_us/", ContactUsApiView.as_view()),
    path("order_place/", OrderPlaceApiView.as_view()),
    path("cradite_purches/", CreditPurchaseApiView.as_view()),
    path("store_registration/", StoreRegistrationApiView.as_view()),
]
