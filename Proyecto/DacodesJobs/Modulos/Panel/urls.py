from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from Modulos.Puestos.views import PanelListPuestos,PanelCreatePuestos,PanelUpdatePuestos
from Modulos.AreasTrabajo.views import PanelListAreas, PanelCreateAreas, PanelUpdateAreas
from Modulos.Empleados.views import PanelListEmpleados


urlpatterns = [
    path('', PanelIndex.as_view(), name = 'PanelIndex'),
    path('Puestos',PanelListPuestos.as_view(), name = 'PanelPuestosListar'),
    path('Puestos/Crear',PanelCreatePuestos.as_view(), name = 'PanelPuestosCrear'),
    path('Puestos/Actualizar/<int:pk>',PanelUpdatePuestos.as_view(), name = 'PanelPuestosActualizar'),
    path('Areas',PanelListAreas.as_view(), name = 'PanelAreasListar'),
    path('Areas/Crear',PanelCreateAreas.as_view(), name = 'PanelAreasCrear'),
    path('Empleados',PanelListEmpleados.as_view(), name = 'PanelEmpleados'),
]
