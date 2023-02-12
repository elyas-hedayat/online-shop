from django.urls import path

from .views import CategoryListApiView

urlpatterns = [
    path("list/", CategoryListApiView.as_view()),
]
