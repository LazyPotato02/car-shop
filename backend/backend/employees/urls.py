from django.urls import path

from backend.employees.views import CreateEmployee, ListEmployees

urlpatterns = [
    path('', ListEmployees.as_view(), name='employee list'),
    path('add/',CreateEmployee.as_view(), name='employee create'),
]