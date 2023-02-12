from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from .models import Message, Ticket
from .serializers import MessageSerializer, TicketDetailSerializer, TicketSerializer


class UserTicketListApiView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = TicketSerializer

    def get_queryset(self):
        query = Ticket.objects.filter(user=self.request.user)
        return query


class TicketRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = TicketDetailSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        query = Ticket.objects.filter(user=self.request.user)
        return query


class TicketCreateApiView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user, status="unread")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class MessageCreateApiView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        return serializer.save(ticket_id=self.kwargs.get("pk"))
