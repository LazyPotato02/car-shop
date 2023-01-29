from django.urls import path

from backend.cells.views import CreateCell

urlpatterns = [
    # path('')
    path('add/', CreateCell.as_view(), name='cell creation')
    # path('remove/')
]
