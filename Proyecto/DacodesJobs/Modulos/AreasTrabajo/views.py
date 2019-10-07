from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

class PanelListAreas(ListView):
    model = AreasTrabajo
    template_name = 'panel/AreasTrabajo/listado.html'
    context_object_name = 'areas'
    queryset = AreasTrabajo.objects.filter(estatus = True)

class PanelCreateAreas(CreateView):
    model = AreasTrabajo
    form_class = AreasForm
    template_name = 'panel/AreasTrabajo/formulario.html'
    success_url = reverse_lazy('Panel:PanelAreasListar')

class PanelUpdateAreas(UpdateView):
    model = AreasTrabajo
    form_class = AreasForm
    template_name = 'panel/AreasTrabajo/formulario.html'
    success_url = reverse_lazy('Panel:PanelAreasListar')
