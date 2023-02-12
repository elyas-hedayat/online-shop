from django.urls import path

from .views import AmazingProductListApiView  # CustomerClubClubListApiView,
from .views import (
    BestSellerProductListApiView,
    MyShopProductListApiView,
    ProductCreateApiView,
    ProductDeleteApiView,
    ProductDetailApiView,
    ProductImageCreateApiView,
    ProductImageDeleteApiView,
    ProductListApiView,
    ProductUpdateApiView,
    PromotionCreateApiView,
    PromotionDeleteApiView,
    PromotionUpdateApiView,
    SuggestionProductListApiView,
    ProductFilterByProvince,
)

urlpatterns = [
    path("list/", ProductListApiView.as_view()),
    path("create/", ProductCreateApiView.as_view()),
    path("update/<int:pk>/", ProductUpdateApiView.as_view()),
    path("detail/<int:pk>", ProductDetailApiView.as_view()),
    path("delete/<int:pk>/", ProductDeleteApiView.as_view()),
    path("suggestion_list/", SuggestionProductListApiView.as_view()),
    path("my_shop/", MyShopProductListApiView.as_view()),
    path("amazing_list/", AmazingProductListApiView.as_view()),
    path("best_seller_list/", BestSellerProductListApiView.as_view()),
    path("promotion_create/", PromotionCreateApiView.as_view()),
    path("promotion_update/<int:pk>/", PromotionUpdateApiView.as_view()),
    path("promotion_delete/<int:pk>/", PromotionDeleteApiView.as_view()),
    path("product_image/<int:pk>/", ProductImageDeleteApiView.as_view()),
    path("product_image_create/", ProductImageCreateApiView.as_view()),
    path("province/<str:state>/", ProductFilterByProvince.as_view()),
    # path("customer_club/", CustomerClubClubListApiView.as_view()),
]
