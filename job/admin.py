from django.contrib import admin

from .models import Apply, Job


class ApplyInline(admin.StackedInline):
    model = Apply
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    inlines = [
        ApplyInline,
    ]
