from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView,CreateView,View
from .models import *
from .forms import *
from Modulos.Puestos.models import Puestos
from django.urls import reverse_lazy

class PanelListCandidatos(ListView):
    model = Candidatos
    template_name = 'panel/Candidatos/listado.html'
    context_object_name = 'candidatos'
    paginate_by = 10
    queryset = Candidatos.objects.filter(estatus = True).order_by('nombre')

class PanelDeleteCandidatos(DeleteView):
    model = Candidatos
    template_name = 'panel/Candidatos/eliminar.html'
    success_url = reverse_lazy('Panel:CandidatosListar')

class Candidatos(CreateView):
    model = Candidatos
    def get(self, request, pk, *args, **kwargs):
        puesto = Puestos.objects.filter(id = pk).get()
        datos = {
            'form': CandidatosPostulacionForm,
            'puesto' : puesto,
        }
        return render(request, 'users/formulario_candidatos.html',datos)

    def post(self, request, pk, *args, **kwargs):
        form = CandidatosPostulacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Puestos:Puestos')
        else:
            datos = {
                'form':form,
            }
            return render(request, 'users/formulario_candidatos.html',datos)
