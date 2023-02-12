from rest_framework.permissions import BasePermission


class ShopAccessPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.status == "business":
            return True
        return False


class ShopCreatePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.status == "client":
            return True
        return False
