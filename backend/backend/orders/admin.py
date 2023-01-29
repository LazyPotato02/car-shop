from django.contrib import admin

from backend.orders.models import Order


# Register your models here.
@admin.register(Order)
class CellAdmin(admin.ModelAdmin):
    pass