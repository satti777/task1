from django.contrib import admin
from .models import Categories, VehicleData

# Register your models here.
admin.site.register(Categories)


@admin.register(VehicleData)
class VhicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'model', 'registration_no', 'category']
