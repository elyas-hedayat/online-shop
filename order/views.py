import logging

from azbankgateways import bankfactories
from azbankgateways import default_settings as settings
from azbankgateways import models as bank_models
from azbankgateways.exceptions import AZBankGatewaysException
from django.db import transaction
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from utilities.bank import create_request, verify_request

from .models import Cheque, Coupon, CustomerClub, Order, OrderItem, PrizeOfBuy
from .serializers import (
    ChequeSerializer,
    CreateOrderSerializer,
    CustomerClubSerializer,
    DiscountCodeSerializer,
    OrderItemSerializer,
    OrderSerializer,
    UpdateOrderSerializer,
)


class ChequeCreateApiView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cheque.objects.all()
    serializer_class = ChequeSerializer

    def perform_create(self, serializer):
        return serializer.save(submitter=self.request.user)


class CustomerClubListApiView(generics.ListAPIView):
    serializer_class = CustomerClubSerializer
    queryset = CustomerClub.objects.all()


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data, context={"user_id": self.request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateOrderSerializer
        elif self.request.method == "PATCH":
            return UpdateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if user.status == "business":
            return Order.objects.all()
        return Order.objects.filter(customer_id=self.request.user)


class MyShopOrderListApiView(generics.ListAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(product__shop=self.request.user.shop)


class CreditBuyApiView(generics.GenericAPIView):
    serializer_class = DiscountCodeSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            if serialized_data.validated_data["code"]:
                try:
                    coupon_obj = Coupon.objects.get(
                        coupon_token=serialized_data.validated_data["code"],
                        user=self.request.user,
                    )
                except:
                    return Response(data={"message": "Coupon is not valid"})
            try:
                cheque_obj = Cheque.objects.get(
                    submitter=self.request.user, status="A", used=False
                )
            except:
                return Response(data={"message": "you can not buy by credit"})
            order_obj = get_object_or_404(Order, pk=kwargs.get("pk"))
            order_item_obj = OrderItem.objects.filter(order=order_obj)
            pay_amount = order_obj.get_total_price()
            if coupon_obj:
                if order_obj.get_total_price() > coupon_obj.minimum_card_amount:
                    pay_amount = order_obj.get_total_price() - coupon_obj.discount_rate
            if all(order_item_obj.values_list("product__credit_sale", flat=True)):
                return Response(
                    data={"message": "credit_sale must be enable for all order item"}
                )
            elif pay_amount > cheque_obj.amount:
                return Response(
                    data={
                        "message": "order total price must me equal or lower than cheque amount"
                    }
                )
            else:
                with transaction.atomic():
                    order_obj.payment_status = "C"
                    order_obj.save()

                    prize_obj = PrizeOfBuy.objects.filter(
                        Q(form_amount__lte=order_obj.get_total_price())
                        | Q(to_amount__gte=order_obj.get_total_price())
                    ).first()
                    request.user.user_point += prize_obj.point
                    request.user.save()
                    for obj in order_obj.items.all():
                        obj.product.remove_items_from_inventory(obj.quantity)
                    return Response(data={"message": "order paid"})


class go_to_gateway_view(generics.GenericAPIView):
    serializer_class = DiscountCodeSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            if serialized_data.validated_data["code"]:
                try:
                    coupon_obj = Coupon.objects.get(
                        coupon_token=serialized_data.validated_data["code"],
                        user=self.request.user,
                    )
                except:
                    return Response(data={"message": "Coupon is not valid"})

        order_obj = get_object_or_404(Order, pk=kwargs.get("pk"))
        amount = order_obj.get_total_price()
        if coupon_obj:
            if order_obj.get_total_price() > coupon_obj.minimum_card_amount:
                amount = order_obj.get_total_price() - coupon_obj.discount_rate

        user_mobile_number = order_obj.phone_number

        factory = bankfactories.BankFactory()
        try:
            bank = factory.create(bank_models.BankType.MELLAT)
            bank.set_request(request)
            bank.set_amount(amount)
            bank.set_client_callback_url(reverse("callback-gateway"))
            bank.set_mobile_number(user_mobile_number)
            bank_record = bank.ready()
            order_obj.payment_tracking_code = bank_record.tracking_code
            order_obj.save()
            return Response(data={"message": "to bank"})
        except AZBankGatewaysException as e:
            logging.critical(e)
            raise e


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404
    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404
    if bank_record.is_success:
        with transaction.atomic():
            order_obj = Order.objects.get(payment_tracking_code=tracking_code)
            order_obj.payment_status = "C"
            order_obj.save()
            prize_obj = PrizeOfBuy.objects.filter(
                Q(form_amount__lte=order_obj.get_total_price())
                | Q(to_amount__gte=order_obj.get_total_price())
            ).first()
            request.user.user_point += prize_obj.point
            request.user.save()
            for obj in order_obj.items.all():
                obj.product.remove_items_from_inventory(obj.quantity)
            return HttpResponse("پرداخت با موفقیت انجام شد.")
    return HttpResponse(
        "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."
    )
