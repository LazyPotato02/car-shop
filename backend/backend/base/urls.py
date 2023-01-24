from django.urls import path

from backend.cells.views import Index

urlpatterns = [
    path('', Index.as_view(), name='home page')
]