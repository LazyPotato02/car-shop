from django.urls import path
from cars.views import CarCreateApiView, CarDetailApiView

urlpatterns =[
    path('api', CarCreateApiView.as_view()),
    path('api/<int:todo_id>/', CarDetailApiView.as_view()),
]