from django.urls import path

from backend.base.views import Index

urlpatterns = [
    path('', Index.as_view(), name='home page')
]