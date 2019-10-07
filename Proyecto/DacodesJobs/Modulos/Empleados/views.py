from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import EmpleadosForm
from django.urls import reverse_lazy

class PanelListEmpleados(ListView):
    model = Empleados
    template_name = 'panel/Empleados/listado.html'
    context_object_name = 'empleados'
    queryset = Empleados.objects.filter(estatus = True)

class PanelCreateEmpleados(CreateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'panel/Empleados/formulario.html'
    success_url = reverse_lazy('Panel:PanelEmpleadosListar')

class PanelUpdateEmpleados(UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'panel/Empleados/formulario.html'
    success_url = reverse_lazy('Panel:PanelEmpleadosListar')
