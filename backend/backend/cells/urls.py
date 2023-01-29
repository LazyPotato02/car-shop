from django.urls import path

from backend.cells.views import CreateCell, ListCell

urlpatterns = [
    path('', ListCell.as_view(), name='cell listing'),
    path('add/', CreateCell.as_view(), name='cell creation')
    # path('remove/')
]
