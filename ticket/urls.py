from django.urls import path

from .views import (
    MessageCreateApiView,
    TicketCreateApiView,
    TicketRetrieveApiView,
    UserTicketListApiView,
)

urlpatterns = [
    path("list/", UserTicketListApiView.as_view()),
    path("detail/<int:pk>/", TicketRetrieveApiView.as_view()),
    path("crate/", TicketCreateApiView.as_view()),
    path("message_crate/<int:pk>", MessageCreateApiView.as_view()),
]
