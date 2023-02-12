from django.urls import path

from .views import (
    MostPopularShopListApiView,
    MySopApiView,
    NewestShopListApiView,
    ShopCreateApiView,
    ShopDetailApiView,
    ShopListApiView,
    ShopProductListApiView,
    ShopUpdateApiView,
)

urlpatterns = [
    path("list/", ShopListApiView.as_view()),
    path("my_shop/", MySopApiView.as_view()),
    path("newest/", NewestShopListApiView.as_view()),
    path("most_popular/", MostPopularShopListApiView.as_view()),
    path("create/", ShopCreateApiView.as_view()),
    path("detail/<int:pk>/", ShopDetailApiView.as_view()),
    path("update/", ShopUpdateApiView.as_view()),
    path("product_list/<int:pk>/", ShopProductListApiView.as_view()),
]
