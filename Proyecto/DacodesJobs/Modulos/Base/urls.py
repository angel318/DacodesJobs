from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', Index.as_view(), name = 'Index'),
    path('Puesto/<int:pk>/', PuestoDetalles.as_view(), name = 'DetallePuesto'),
    path('Puestos', PuestosPublicados.as_view(), name = 'Puestos'),
    path('Nosotros', Nosotros.as_view(), name = 'Nosotros'),
    path('busqueda/', Busqueda, name='Busqueda'),
    path('Staff/',login_required(StaffIndex.as_view()), name = 'StaffIndex'),
]
