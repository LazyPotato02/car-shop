from django.contrib import admin

from backend.cells.models import Cells


# Register your models here.
@admin.register(Cells)
class CellAdmin(admin.ModelAdmin):
    pass