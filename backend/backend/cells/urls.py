from django.urls import path

from backend.cells.views import CreateCell, ListCell, EditCell

urlpatterns = [
    path('', ListCell.as_view(), name='cell listing'),
    path('add/', CreateCell.as_view(), name='cell creation'),
    path('edit/<int:pk>', EditCell.as_view(), name='cell edit')
    # path('remove/')
]
