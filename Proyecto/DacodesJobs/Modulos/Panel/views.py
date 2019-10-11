from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from Modulos.Empleados.models import Empleados
from Modulos.Candidatos.models import Candidatos
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Puestos.models import Puestos

#Vistas
class PanelIndex(TemplateView):
    def get(self,request,*args,**kwargs):

        topEmpleados = list(Empleados.objects.order_by('-salario'))
        empleadosCount = Empleados.objects.count()
        candidatosCount = Candidatos.objects.count()
        areasCount = AreasTrabajo.objects.count()
        puestosCount = Puestos.objects.count()

        datos = {
            'topEmpleados' : topEmpleados,
            'empleadosCount' : empleadosCount,
            'candidatosCount' : candidatosCount,
            'areasCount' : areasCount,
            'puestosCount' : puestosCount,
        }
        return render(request, 'panel/index.html', datos)
