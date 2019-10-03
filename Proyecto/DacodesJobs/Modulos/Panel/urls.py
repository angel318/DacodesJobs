from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from Modulos.Puestos.views import AdminListPuestos
from Modulos.AreasTrabajo.views import AdminListAreas

urlpatterns = [
    path('', PanelIndex.as_view(), name = 'PanelIndex'),
    path('Puestos',AdminListPuestos.as_view(), name = 'PanelPuestosPublicados'),
    path('Areas',AdminListAreas.as_view(), name = 'PanelAreasTrabajo')
]
