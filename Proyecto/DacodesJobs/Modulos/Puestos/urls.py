from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('',  PuestosPublicados.as_view(), name = 'Puestos'),
    path('busqueda/', Busqueda, name='Busqueda'),
    path('<int:pk>/', PuestoDetalles.as_view(), name = 'DetallePuesto'),
]
