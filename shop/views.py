from rest_framework import generics

from product.models import Product
from product.serializers import ProductDetailSerializer
from shop.models import Shop

from .permission import ShopAccessPermission, ShopCreatePermission
from .serializers import ShopMainSerializer, ShopSerializer


class ShopCreateApiView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [
        ShopCreatePermission,
    ]

    def perform_create(self, serializer):
        self.request.user.status = "business"
        self.request.user.save()
        return serializer.save(user=self.request.user)


class ShopUpdateApiView(generics.UpdateAPIView):
    serializer_class = ShopSerializer
    permission_classes = [
        ShopAccessPermission,
    ]

    def get_object(self):
        return Shop.objects.get(user=self.request.user)


class ShopListApiView(generics.ListAPIView):
    queryset = Shop.objects.active()
    serializer_class = ShopMainSerializer


class ShopDetailApiView(generics.RetrieveAPIView):
    queryset = Shop.objects.active()
    serializer_class = ShopSerializer


class MySopApiView(generics.RetrieveAPIView):
    serializer_class = ShopSerializer
    permission_classes = [
        ShopAccessPermission,
    ]

    def get_object(self):
        return Shop.objects.get(user=self.request.user)


class ShopProductListApiView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        return Product.objects.filter(shop_id=self.kwargs.get("pk"))


class NewestShopListApiView(generics.ListAPIView):
    queryset = Shop.objects.filter(newest_shop=True)
    serializer_class = ShopMainSerializer


class MostPopularShopListApiView(generics.ListAPIView):
    queryset = Shop.objects.filter(most_popular=True)
    serializer_class = ShopMainSerializer
