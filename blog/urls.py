from django.urls import path

from .views import BlogDetailApiView, BlogListApiView

urlpatterns = [
    path("list/", BlogListApiView.as_view()),
    path("detail/<int:pk>/", BlogDetailApiView.as_view()),
]
