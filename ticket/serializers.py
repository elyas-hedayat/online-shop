from drf_extra_fields.fields import Base64ImageField
from jalali_date import date2jalali
from rest_framework import serializers

from .models import Document, Message, Ticket


class UploadedBase64ImageSerializer(serializers.Serializer):
    file = Base64ImageField(required=False)


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "id",
            "file",
        )


class MessageSerializer(serializers.ModelSerializer):
    document = UploadedBase64ImageSerializer()

    class Meta:
        model = Message
        fields = (
            "id",
            "message",
            "document",
        )

    def create(self, validated_data):
        document_list = []
        document_obj = validated_data.pop("document")
        message_obj = Message.objects.create(**validated_data)
        for valid_data in document_obj:
            document_list.append(Document(message=message_obj, **valid_data))
        Document.objects.bulk_create(document_list)
        return validated_data


class TicketSerializer(serializers.ModelSerializer):
    document = UploadedBase64ImageSerializer(many=True, write_only=True)
    message = serializers.CharField(write_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "title",
            # "user",
            "status",
            "priority",
            "ticket_number",
            "document",
            "message",
        )
        # read_only_fields = ("user",)

    def create(self, validated_data):
        document_list = []
        document_obj = validated_data.pop("document")
        message_data = validated_data.pop("message")
        ticket_obj = Ticket.objects.create(**validated_data)
        message_obj = Message.objects.create(message=message_data, ticket=ticket_obj)
        for valid_data in document_obj:
            document_list.append(Document(message=message_obj, **valid_data))
        Document.objects.bulk_create(document_list)
        return ticket_obj


class MessageDetailSerializer(serializers.ModelSerializer):
    document = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = (
            "id",
            "message",
            "sender",
            "document",
        )

    def get_document(self, obj):
        return DocumentSerializer(
            Document.objects.filter(message_id=obj.id), many=True
        ).data


class TicketDetailSerializer(serializers.ModelSerializer):
    message_list = serializers.SerializerMethodField(read_only=True)

    created = serializers.SerializerMethodField()
    last_update = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = (
            "id",
            "title",
            "user",
            "status",
            "priority",
            "ticket_number",
            "message_list",
            "created",
            "last_update",
        )
        read_only_fields = (
            "message_list",
            "created",
            "last_update",
        )

    def get_created(self, obj):
        create_time = Message.objects.filter(ticket_id=obj.id).first().created
        date_to_jalali = date2jalali(create_time)
        return date_to_jalali.strftime("%Y/%m/%d")

    def get_last_update(self, obj):
        last_update_time = Message.objects.filter(ticket_id=obj.id).first().created
        date_to_jalali = date2jalali(last_update_time)
        return date_to_jalali.strftime("%Y/%m/%d")

    def get_message_list(self, obj):
        return MessageDetailSerializer(
            Message.objects.filter(ticket_id=obj.id), many=True
        ).data
