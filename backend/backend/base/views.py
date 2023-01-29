from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.
class Index(views.TemplateView):
    template_name = 'base/index.html'
