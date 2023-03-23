from django.contrib import admin

from cars.models import Cars


# Register your models here.
@admin.register(Cars)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("make","model","year","engine_type","user")
