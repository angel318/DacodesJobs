from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from .models import *

class PanelListEmpleados(ListView):
    model = Empleados
    template_name = 'panel/Empleados/listado.html'
    context_object_name = 'empleados'
    queryset = Empleados.objects.filter(estatus = True)
