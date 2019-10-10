from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('',  PuestosPublicados.as_view(), name = 'Puestos'),
    path('<int:pk>/', PuestoDetalles.as_view(), name = 'DetallePuesto'),
    path('busqueda/', Buscador.as_view(), name='Busqueda'),
]
