from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic as views

from backend.cells.forms import CellForm
from backend.cells.models import Cells


# Create your views here.


class CreateCell(LoginRequiredMixin, views.CreateView):
    model = Cells
    form_class = CellForm
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('cell listing')
    template_name = 'cells/cell-create.html'
    success_url = reverse_lazy('cell listing')


class ListCell(LoginRequiredMixin, views.ListView):
    model = Cells
    login_url = reverse_lazy('login')
    template_name = 'cells/cell-list.html'
