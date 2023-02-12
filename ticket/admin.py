from django.contrib import admin

from .models import Document, Message, Ticket

# admin.site.register(Document)
# admin.site.register(Message)
# admin.site.register(Ticket)


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0


class MessageAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    fields = ("message", "changeform_link", "sender")
    inlines = [
        DocumentInline,
    ]
    readonly_fields = ("sender", "changeform_link")


admin.site.register(Message, MessageAdmin)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    inlines = [
        MessageInline,
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
