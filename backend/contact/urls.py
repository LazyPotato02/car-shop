from django.urls import path

from contact.views import ContactsCreateApiView, ContactDetailApiView

urlpatterns =[
    path('api', ContactsCreateApiView.as_view()),
    path('api/<int:todo_id>/', ContactDetailApiView.as_view()),
]