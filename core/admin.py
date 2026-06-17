from django.contrib import admin
from .models import Vehicle, VehicleImage, Enquiry

class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 1

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageInline]

admin.site.register(Enquiry)