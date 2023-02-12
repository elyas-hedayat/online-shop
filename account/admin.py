from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import ChangeForm, CreateForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = ChangeForm
    add_form = CreateForm

    list_display = ("phone_number", "is_admin")
    list_filter = ("is_admin",)
    readonly_fields = (
        "last_login",
        "user_point",
        "user_wallet",
        "phone_number",
        "first_name",
        "last_name",
    )

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    "phone_number",
                    "first_name",
                    "last_name",
                    "user_point",
                    "user_wallet",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "status",
                    "is_active",
                    "is_admin",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (None, {"fields": ("phone_number", "password", "password_confirm")}),
    )

    search_fields = ("phone_number",)
    ordering = ("phone_number",)
    filter_horizontal = ("groups", "user_permissions")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields["is_superuser"].disabled = True
            form.base_fields["status"].disabled = True
        return form


admin.site.register(User, UserAdmin)
