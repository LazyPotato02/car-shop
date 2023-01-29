from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from backend.base.views import Index

urlpatterns = [
    path('', Index.as_view(), name='home page'),
    path('login', auth_views.LoginView.as_view(template_name='base/login.html', success_url=reverse_lazy('index'),
                                               redirect_authenticated_user=True), name='login'),

]