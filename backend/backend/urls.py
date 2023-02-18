from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.base.urls')),
    path('cells/', include('backend.cells.urls')),
    path('employees/', include('backend.employees.urls')),
    path('materials/', include('backend.materials.urls')),
    path('orders/', include('backend.orders.urls'))
]
