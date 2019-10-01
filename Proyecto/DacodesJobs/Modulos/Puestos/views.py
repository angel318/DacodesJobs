from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView,View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
import json
from .models import *
from Modulos.Base.models import *
from Modulos.Base.views import consultaDatosEmpresa
from Modulos.AreasTrabajo.models import *
from .forms import *

#Todos los puestos
class PuestosPublicados(ListView):
    def get(self,request,*args,**kwargs):

        puestos = list(Puestos.objects.filter(
            estatus = True,
            disponible = True
        ))

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

#Buscador
def Busqueda(request):
    data_json = None
    if request.is_ajax:
        search = request.GET.get('search','')

        puestos = Puestos.objects.filter(nombre__icontains=search)

        results = []

        for puesto in puestos:
            puesto_json={}
            puesto_json['id'] = puesto.id
            puesto_json['nombre'] = puesto.nombre
            results.append(puesto_json)

        data_json = json.dumps(results)
        print(data_json)
    else:
        data_jason = 'fail'

    mimetype = "application/json"
    return HttpResponse(data_json,mimetype)
