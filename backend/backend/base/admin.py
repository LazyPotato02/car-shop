from django.contrib import admin

from backend.base.models import EmployeeManager


# Register your models here.
@admin.register(EmployeeManager)
class CellAdmin(admin.ModelAdmin):
    pass
