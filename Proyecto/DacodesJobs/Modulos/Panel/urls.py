from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from Modulos.Puestos.views import PanelListPuestos, PanelCreatePuestos, PanelUpdatePuestos, PanelDeletePuestos
from Modulos.AreasTrabajo.views import PanelListAreas, PanelCreateAreas, PanelUpdateAreas, PanelDeleteAreas
from Modulos.Empleados.views import PanelListEmpleados, PanelCreateEmpleados, PanelUpdateEmpleados, PanelDeleteEmpleados


urlpatterns = [
    path('', PanelIndex.as_view(), name = 'Index'),
    #Puestos
    path('Puestos',PanelListPuestos.as_view(), name = 'PuestosListar'),
    path('Puestos/Crear',PanelCreatePuestos.as_view(), name = 'PuestosCrear'),
    path('Puestos/Actualizar/<int:pk>',PanelUpdatePuestos.as_view(), name = 'PuestosActualizar'),
    path('Puestos/Eliminar/<int:pk>',PanelDeletePuestos.as_view(), name = 'PuestosEliminar'),
    #Areas Trabajo
    path('Areas',PanelListAreas.as_view(), name = 'AreasListar'),
    path('Areas/Crear',PanelCreateAreas.as_view(), name = 'AreasCrear'),
    path('Areas/Actualizar/<int:pk>',PanelUpdateAreas.as_view(), name = 'AreasActualizar'),
    path('Areas/Eliminar/<int:pk>',PanelDeleteAreas.as_view(), name = 'AreasEliminar'),
    #Empleados
    path('Empleados',PanelListEmpleados.as_view(), name = 'EmpleadosListar'),
    path('Empleados/Crear',PanelCreateEmpleados.as_view(), name = 'EmpleadosCrear'),
    path('Empleados/Actualizar/<int:pk>',PanelUpdateEmpleados.as_view(), name = 'EmpleadosActualizar'),
    path('Empleados/Eliminar/<int:pk>',PanelDeleteEmpleados.as_view(), name = 'EmpleadosEliminar'),
]
