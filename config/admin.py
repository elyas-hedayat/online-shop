from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from .models import (
    AboutUs,
    ContactUs,
    CreditPurchase,
    OrderPlacing,
    Rule,
    Slider,
    StoreRegistration,
)

admin.site.register(AboutUs)
admin.site.register(Rule)
admin.site.register(StoreRegistration)
admin.site.register(CreditPurchase)
admin.site.register(OrderPlacing)
admin.site.register(Slider)
admin.site.register(ContactUs)

AdminSite.site_header = "پلاست اپ"
AdminSite.site_title = "پلاست اپ"
