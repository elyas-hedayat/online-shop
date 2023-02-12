from rest_framework import generics
from rest_framework.response import Response

from .models import AdvertisingBanner, NoticeBanner, PartialData
from .serializers import (
    AdvertisingBannerSerializer,
    NoticeBannerSerializer,
    PartialDataSerializer,
)


class NoticeBannerApiView(generics.GenericAPIView):
    serializer_class = NoticeBannerSerializer
    queryset = NoticeBanner.load()

    def get(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(
            NoticeBanner.load(), context={"request": request}
        ).data
        return Response(data={"data": serialized_data})


class AdvertisingBannerApiView(generics.GenericAPIView):
    serializer_class = AdvertisingBannerSerializer

    def get(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(AdvertisingBanner.load()).data
        return Response(data={"data": serialized_data})


class PartialDataApiView(generics.GenericAPIView):
    serializer_class = PartialDataSerializer
    queryset = PartialData.load()

    def get(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(PartialData.load()).data
        return Response(data={"data": serialized_data})
