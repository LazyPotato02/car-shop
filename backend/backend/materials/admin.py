from django.contrib import admin

from backend.materials.models import Materials


# Register your models here.
@admin.register(Materials)
class CellAdmin(admin.ModelAdmin):
    pass