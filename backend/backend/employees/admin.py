from django.contrib import admin

from backend.employees.models import Employee


# Register your models here.
@admin.register(Employee)
class CellAdmin(admin.ModelAdmin):
    pass