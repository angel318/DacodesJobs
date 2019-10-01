from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView,View
from .models import *
from .forms import *
import random
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
import json

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

#Puesto publicado
class PuestoDetalles(View):
    def get(self,request,pk,*args,**kwargs):
        puesto = Puestos.objects.get(id = pk)

        otrosPuestos = list(Puestos.objects.filter(
            estatus = True,
            disponible = True,
        ).exclude(id=pk))[:5]

        datos = {
            'puesto' : puesto,
            'empresa' : consultaDatosEmpresa(),
            'otrosPuestos':otrosPuestos
        }

        return render(request,'users/puesto_detalles.html',datos)

#Todos los puestos
class PuestosPublicados(ListView):
    def get(self,request,*args,**kwargs):

        puestos = list(Puestos.objects.filter(
            estatus = True,
            disponible = True
        ))

        areas = AreasTrabajo.objects.all().filter(
            estatus = True
        ).values_list('nombre',flat = True).count()

        form = BuscadorForm()

        datos = {
            'puestos' : puestos,
            'empresa' : consultaDatosEmpresa(),
            'form': form,
        }

        return render(request, 'users/puestos.html', datos)

    def post(self,request,*args,**kwargs):
        form1 = BuscadorForm(request.POST)
        if form1.is_valid():
            puesto = Puestos.objects.filter(nombre__icontains=form1.cleaned_data['nombre'])
            form = BuscadorForm()
            datos = {
                'puestos' : puesto,
                'empresa' : consultaDatosEmpresa(),
                'form': form,
            }
            return render(request,'users/puestos.html',datos)
        else:
            datos = {
                'form':form,
            }
            return render(request,'users/puestos.html',datos)

class Nosotros(View):
    def get(self,request,*args,**kwargs):
        datos = {
            'empresa' : consultaDatosEmpresa(),
        }
        return render(request, 'users/nosotros.html', datos)

#Buscador
def Busqueda(request):
    data_json = None
    if request.is_ajax:
        search = request.GET.get('start','')

        puestos = Puestos.objects.filter(nombre__icontains=search)

        results = []

        for puesto in puestos:
            puesto_json={}
            puesto_json['id'] = puesto.id
            puesto_json['nombre'] = puesto.nombre
            results.append(puesto_json)

        data_json = json.dumps(results)

    else:
        data_jason = 'fail'

    mimetype = "application/json"
    return HttpResponse(data_json,mimetype)



##Staff

class StaffIndex(TemplateView):
    template_name = 'Staff/index.html'
