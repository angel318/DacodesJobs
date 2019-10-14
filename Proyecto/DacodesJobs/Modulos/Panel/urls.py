from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from Modulos.Puestos.views import PanelListPuestos, PanelCreatePuestos, PanelUpdatePuestos, PanelDeletePuestos
from Modulos.AreasTrabajo.views import PanelListAreas, PanelCreateAreas, PanelUpdateAreas, PanelDeleteAreas
from Modulos.Empleados.views import PanelListEmpleados, PanelCreateEmpleados, PanelUpdateEmpleados, PanelDeleteEmpleados
from Modulos.Candidatos.views import PanelListCandidatos, PanelDeleteCandidatos
from Modulos.Base.views import PanelDatosEmpresa

urlpatterns = [
    path('', login_required(PanelIndex.as_view()), name = 'Index'),
    #Puestos
    path('Puestos',login_required(PanelListPuestos.as_view()), name = 'PuestosListar'),
    path('Puestos/Crear',login_required(PanelCreatePuestos.as_view()), name = 'PuestosCrear'),
    path('Puestos/Actualizar/<int:pk>',login_required(PanelUpdatePuestos.as_view()), name = 'PuestosActualizar'),
    path('Puestos/Eliminar/<int:pk>',login_required(PanelDeletePuestos.as_view()), name = 'PuestosEliminar'),
    #Areas Trabajo
    path('Areas',login_required(PanelListAreas.as_view()), name = 'AreasListar'),
    path('Areas/Crear',login_required(PanelCreateAreas.as_view()), name = 'AreasCrear'),
    path('Areas/Actualizar/<int:pk>',login_required(PanelUpdateAreas.as_view()), name = 'AreasActualizar'),
    path('Areas/Eliminar/<int:pk>',login_required(PanelDeleteAreas.as_view()), name = 'AreasEliminar'),
    #Empleados
    path('Empleados',login_required(PanelListEmpleados.as_view()), name = 'EmpleadosListar'),
    path('Empleados/Crear',login_required(PanelCreateEmpleados.as_view()), name = 'EmpleadosCrear'),
    path('Empleados/Actualizar/<int:pk>',login_required(PanelUpdateEmpleados.as_view()), name = 'EmpleadosActualizar'),
    path('Empleados/Eliminar/<int:pk>',login_required(PanelDeleteEmpleados.as_view()), name = 'EmpleadosEliminar'),
    #Candidatos
    path('Candidatos/',login_required(PanelListCandidatos.as_view()), name = 'CandidatosListar'),
    #Datos empresa
    path('Datos_de_la_empresa',login_required(PanelDatosEmpresa.as_view()), name = 'DatosEmpresa'),
]
