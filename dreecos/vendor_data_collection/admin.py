from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.Menu)
admin.site.register(models.Submitters)
admin.site.register(models.GeoLocation)
admin.site.register(models.VendorImage)
