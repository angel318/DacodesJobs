from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView,View
from .models import *

class AdminListAreas(ListView):
    model = AreasTrabajo
    template_name = 'panel/AreasTrabajo/areas.html'
    context_object_name = 'areas'
    queryset = AreasTrabajo.objects.filter(estatus = True)
