from django.urls import path

from .views import AdvertisingBannerApiView, NoticeBannerApiView, PartialDataApiView

urlpatterns = [
    path("adv_banner/", AdvertisingBannerApiView.as_view()),
    path("notice_banner/", NoticeBannerApiView.as_view()),
    path("partial_data/", PartialDataApiView.as_view()),
]
