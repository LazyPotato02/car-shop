from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from backend.employees.forms import EmployeeForm
from backend.employees.models import Employee


# Create your views here.
class CreateEmployee(views.CreateView):
    model = Employee
    form_class = EmployeeForm
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('home page')
    template_name = 'employee/employee-create.html'
    success_url = reverse_lazy('home page')

class ListEmployees(views.ListView):
    model = Employee
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('home page')
    template_name = 'employee/employee-list.html'
    success_url = reverse_lazy('home page')
