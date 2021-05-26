from django.urls import path
from .views import (
    CreateCoche, 
    CreateCamioneta, 
    CreateBicicleta, 
    CreateMotocicleta, 
    UpdateCoche, 
    UpdateCamioneta, 
    UpdateBicicleta, 
    UpdateMotocicleta,
    ListVehicle,
)

vehicle_patterns = [
    path('create-coche', CreateCoche.as_view(), name="create-coche"),
    path('update-coche/<int:pk>/', UpdateCoche.as_view(), name="update-coche"),

    path('create-camioneta', CreateCamioneta.as_view(), name="create-camioneta"),
    path('update-camioneta/<int:pk>/', UpdateCamioneta.as_view(), name="update-camioneta"),


    path('create-bicicleta', CreateBicicleta.as_view(), name="create-bicicleta"),
    path('update-bicicleta/<int:pk>/', UpdateBicicleta.as_view(), name="update-bicicleta"),


    path('create-motocicleta', CreateMotocicleta.as_view(), name="create-motocicleta"),
    path('update-motocicleta/<int:pk>/', UpdateMotocicleta.as_view(), name="update-motocicleta"),

    path('list-vehicle', ListVehicle.as_view(), name="list-vehicle"),

]