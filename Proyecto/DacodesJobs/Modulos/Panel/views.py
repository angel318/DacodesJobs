from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from Modulos.Empleados.models import Empleados
from Modulos.Candidatos.models import Candidatos
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Puestos.models import Puestos

#Vistas
class PanelIndex(TemplateView):
    def get(self,request,*args,**kwargs):

        topEmpleados = list(Empleados.objects.order_by('-salario'))[:10]
        empleadosCount = Empleados.objects.count()
        candidatosCount = Candidatos.objects.count()
        areasCount = AreasTrabajo.objects.count()
        puestosCount = Puestos.objects.count()

        grafica = Empleados.objects.values_list('puesto_id').distinct()
        grafica2 = {}
        for graf in grafica:
            variable = AreasTrabajo.objects.filter(id = graf[0]).get()
            grafica2[variable.nombre] = Empleados.objects.filter(puesto = graf).count()
        datos = {
            'topEmpleados' : topEmpleados,
            'empleadosCount' : empleadosCount,
            'candidatosCount' : candidatosCount,
            'areasCount' : areasCount,
            'puestosCount' : puestosCount,
            'grafica2' :grafica2
        }
        return render(request, 'panel/index.html', datos)
