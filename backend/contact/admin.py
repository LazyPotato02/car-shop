from django.contrib import admin

from contact.models import Contact


# Register your models here.
@admin.register(Contact)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("email","name","text","user")
