from django.urls import path

from backend.employees.views import CreateEmployee

urlpatterns = [
    path('add/',CreateEmployee.as_view(), name='create employee'),
]