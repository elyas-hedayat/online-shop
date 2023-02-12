from django.urls import path
from rest_framework_nested import routers

from .views import (
    ChequeCreateApiView,
    CreditBuyApiView,
    CustomerClubListApiView,
    MyShopOrderListApiView,
    OrderViewSet,
    callback_gateway_view,
    go_to_gateway_view,
)

router = routers.DefaultRouter()
router.register("orders", OrderViewSet, basename="orders")
urlpatterns = [
    path("check_create/", ChequeCreateApiView.as_view()),
    path("coustomer_club_list/", CustomerClubListApiView.as_view()),
    path("my_shop_order/", MyShopOrderListApiView.as_view()),
    path("credit_buy/<int:pk>/", CreditBuyApiView.as_view()),
    path("to_bank/<int:pk>/", go_to_gateway_view.as_view()),
    path("bank_verify/<int:pk>/", callback_gateway_view),
]

urlpatterns += router.urls
