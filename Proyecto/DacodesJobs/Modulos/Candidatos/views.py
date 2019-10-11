from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import *
from .forms import *
from Modulos.Puestos.models import Puestos

class Candidatos(CreateView):
    model = Candidatos
    def get(self, request, pk, *args, **kwargs):
        puesto = Puestos.objects.filter(id = pk).get()
        datos = {
            'form': CandidatosForm,
            'puesto' : puesto,
        }
        return render(request, 'users/formulario_candidatos.html',datos)

    def post(self, request, pk, *args, **kwargs):
        form = CandidatosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Puestos:Puestos')
        else:
            datos = {
                'form':form,
            }
            return render(request, 'users/formulario_candidatos.html',datos)
