import django.contrib.auth.views
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.
class Index(views.TemplateView):
    template_name = 'base/index.html'


