from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
import random
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

        puestos = list(Puestos.objects.filter(
            estatus = True,
            disponible = True
        ))[:1]

        areas = list(AreasTrabajo.objects.filter(
                    estatus = True,
        ))

        datos = {
            'puestos' : puestos,
            'areas' : areas,
            'empresa' : consultaDatosEmpresa(),
        }

        return render(request, 'index.html', datos)

class Nosotros(View):
    def get(self,request,*args,**kwargs):
        datos = {
            'empresa' : consultaDatosEmpresa(),
        }
        return render(request, 'users/nosotros.html', datos)


##Staff

class StaffIndex(TemplateView):
    template_name = 'Staff/index.html'
