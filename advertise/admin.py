from django.contrib import admin

from .models import AdvertisingBanner, NoticeBanner, PartialData

admin.site.register(AdvertisingBanner)
admin.site.register(NoticeBanner)
admin.site.register(PartialData)
