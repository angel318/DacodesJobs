from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from Modulos.Empleados.models import Empleados

#Vistas
class PanelIndex(TemplateView):
    def get(self,request,*args,**kwargs):
        
        topEmpleados = list(Empleados.objects.order_by('-salario'))

        datos = {
            'topEmpleados' : topEmpleados,
        }
        return render(request, 'panel/index.html', datos)
