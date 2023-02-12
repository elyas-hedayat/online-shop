from django.urls import path

from .views import ApplyCreateApiView, JobListApiView

urlpatterns = [
    path("list/", JobListApiView.as_view()),
    path("apply/", ApplyCreateApiView.as_view()),
]
