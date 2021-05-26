from django.contrib import admin
from django.urls import path, include
from core.views import home
from vehicle.urls import vehicle_patterns


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('vehicle/', include(vehicle_patterns)),
]
