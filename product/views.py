from rest_framework import filters, generics

from shop.permission import ShopAccessPermission

from .models import Product, ProductImage, Promotion
from .serializers import ProductCreateSerializer  # CustomerClubSerializer,
from .serializers import (
    ImageSerializer,
    ProductDetailSerializer,
    ProductMainSerializer,
    PromotionSerializer,
)


class ProductImageDeleteApiView(generics.DestroyAPIView):
    permission_classes = [
        ShopAccessPermission,
    ]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product__shop=self.request.user.shop)


class ProductImageCreateApiView(generics.CreateAPIView):
    permission_classes = [
        ShopAccessPermission,
    ]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product__shop=self.request.user.shop)


class ProductListApiView(generics.ListAPIView):
    """
    list all active product
    """

    queryset = Product.objects.active()
    serializer_class = ProductMainSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "@title",
    ]


class ProductDetailApiView(generics.RetrieveAPIView):
    """
    detail view for active products
    """

    queryset = Product.objects.active()
    serializer_class = ProductDetailSerializer


class ProductCreateApiView(generics.CreateAPIView):
    """
    create product (access just for client that their status equal to business)
    """

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [
        ShopAccessPermission,
    ]

    def perform_create(self, serializer):
        return serializer.save(shop=self.request.user.shop)


class ProductUpdateApiView(generics.UpdateAPIView):
    """
    update user product info
    """

    permission_classes = [
        ShopAccessPermission,
    ]
    serializer_class = ProductCreateSerializer

    def get_queryset(self):
        return Product.objects.filter(shop=self.request.user.shop)


class ProductDeleteApiView(generics.DestroyAPIView):
    """
    delete user product
    """

    permission_classes = [
        ShopAccessPermission,
    ]
    serializer_class = ProductMainSerializer

    def get_queryset(self):
        return Product.objects.filter(shop=self.request.user.shop)


class ProductFilterByProvince(generics.ListAPIView):
    def get_queryset(self):
        return Product.objects.filter(shop__state=self.kwargs.get('state'))

    serializer_class = ProductMainSerializer


class MyShopProductListApiView(generics.ListAPIView):
    permission_classes = [
        ShopAccessPermission,
    ]
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        return Product.objects.filter(shop=self.request.user.shop)


class SuggestionProductListApiView(generics.ListAPIView):
    serializer_class = ProductMainSerializer

    def get_queryset(self):
        return Product.objects.filter(suggestion=True)


class AmazingProductListApiView(generics.ListAPIView):
    serializer_class = ProductMainSerializer

    def get_queryset(self):
        return Product.objects.filter(amazing=True)


class BestSellerProductListApiView(generics.ListAPIView):
    serializer_class = ProductMainSerializer

    def get_queryset(self):
        return Product.objects.filter(best_seller=True)


class PromotionCreateApiView(generics.CreateAPIView):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()


class PromotionUpdateApiView(generics.UpdateAPIView):
    serializer_class = PromotionSerializer
    permission_classes = [
        ShopAccessPermission,
    ]

    def get_queryset(self):
        return Promotion.objects.filter(product__shop__user=self.request.user)


class PromotionDeleteApiView(generics.DestroyAPIView):
    serializer_class = PromotionSerializer
    permission_classes = [
        ShopAccessPermission,
    ]

    def get_queryset(self):
        return Promotion.objects.filter(product__shop__user=self.request.user)

#
# class CustomerClubClubListApiView(generics.ListAPIView):
#     queryset = CustomerClub.objects.all()
#     serializer_class = CustomerClubSerializer
