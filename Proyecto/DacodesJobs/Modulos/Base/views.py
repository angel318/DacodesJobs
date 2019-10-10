from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
#MODELOS
from .models import *
from Modulos.Puestos.forms import *
from Modulos.AreasTrabajo.models import *
from Modulos.Empleados.models import *

# Create your views here.
def consultaDatosEmpresa():
    try:
        return DatosEmpresa.objects.get()
    except:
        return None

#Inicio
class Index(ListView):
    def get(self,request,*args,**kwargs):

        puestos = Puestos.objects.filter(
            estatus = True,
            disponible = True
        )[:1]

        areas = list(AreasTrabajo.objects.filter(
                    estatus = True,
        ).order_by('nombre'))[:3]

        datos = {
            'puestos' : puestos,
            'areas' : areas,
            'empresa' : consultaDatosEmpresa(),
        }

        return render(request, 'users/index.html', datos)


#Informacion de la empresa
class Nosotros(View):
    def get(self,request,*args,**kwargs):
        datos = {
            'empresa' : consultaDatosEmpresa(),
        }
        return render(request, 'users/nosotros.html', datos)
