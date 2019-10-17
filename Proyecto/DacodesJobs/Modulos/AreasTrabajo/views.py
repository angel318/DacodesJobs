from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.paginator import Paginator

#Areas de trabajo
class Areas(ListView):
    def get(self,request,*args,**kwargs):
        areas = list(AreasTrabajo.objects.filter(
                    estatus = True,
        ).order_by('nombre'))

        datos = {
            "areas" : areas
        }

        return render(request, 'users/areas.html', datos)

class PanelListAreas(ListView):
    model = AreasTrabajo
    template_name = 'panel/AreasTrabajo/listado.html'
    context_object_name = 'areas'
    paginate_by = 6
    queryset = AreasTrabajo.objects.filter(estatus = True).order_by('nombre')

class PanelCreateAreas(CreateView):
    model = AreasTrabajo
    form_class = AreasForm
    template_name = 'panel/AreasTrabajo/formulario.html'
    success_url = reverse_lazy('Panel:AreasListar')

class PanelUpdateAreas(UpdateView):
    model = AreasTrabajo
    form_class = AreasForm
    template_name = 'panel/AreasTrabajo/formulario.html'
    success_url = reverse_lazy('Panel:AreasListar')

class PanelDeleteAreas(DeleteView):
    model = AreasTrabajo
    template_name = 'panel/AreasTrabajo/eliminar.html'
    success_url = reverse_lazy('Panel:AreasListar')
