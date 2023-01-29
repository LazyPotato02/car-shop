from django import forms

from backend.cells.models import Cells


class CellForm(forms.ModelForm):
    class Meta:
        model = Cells
        fields = "__all__"
