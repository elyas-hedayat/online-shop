from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics
from rest_framework.response import Response

from .models import (
    AboutUs,
    ContactUs,
    CreditPurchase,
    OrderPlacing,
    Rule,
    Slider,
    StoreRegistration,
)
from .serializers import (
    AboutUsSerializer,
    ConfigSerializer,
    ContactUsSerializer,
    CreditPurchaseSerializer,
    OrderPlaceSerializer,
    RuleSerializer,
    SliderSerializer,
)


class RuleApiView(generics.GenericAPIView):
    serializer_class = RuleSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Rule.load())
        return Response(data={"data": serializer.data})


class AboutUsApiView(generics.GenericAPIView):
    serializer_class = AboutUsSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(AboutUs.load())
        return Response(data={"data": serializer.data})


class OrderPlaceApiView(generics.GenericAPIView):
    serializer_class = OrderPlaceSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(OrderPlacing.load())
        return Response(data={"data": serializer.data})


class CreditPurchaseApiView(generics.GenericAPIView):
    serializer_class = CreditPurchaseSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(CreditPurchase.load())
        return Response(data={"data": serializer.data})


class StoreRegistrationApiView(generics.GenericAPIView):
    serializer_class = ConfigSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(StoreRegistration.load())
        return Response(data={"data": serializer.data})


class ContactUsApiView(generics.GenericAPIView):
    serializer_class = ContactUsSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(ContactUs.load())
        return Response(data={"data": serializer.data})


class SliderListApiView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
