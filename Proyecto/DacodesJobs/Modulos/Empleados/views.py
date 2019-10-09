from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import EmpleadosForm
from django.urls import reverse_lazy

class PanelListEmpleados(ListView):
    model = Empleados
    template_name = 'panel/Empleados/listado.html'
    context_object_name = 'empleados'
    paginate_by = 10
    queryset = Empleados.objects.filter(estatus = True).order_by('nombre')

class PanelCreateEmpleados(CreateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'panel/Empleados/formulario.html'
    success_url = reverse_lazy('Panel:EmpleadosListar')

class PanelUpdateEmpleados(UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'panel/Empleados/formulario.html'
    success_url = reverse_lazy('Panel:EmpleadosListar')

class PanelDeleteEmpleados(DeleteView):
    model = Empleados
    template_name = 'panel/Empleados/eliminar.html'
    success_url = reverse_lazy('Panel:EmpleadosListar')
