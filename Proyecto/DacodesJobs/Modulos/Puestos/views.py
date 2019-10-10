from django.shortcuts import render
from django.views.generic import ListView,UpdateView,CreateView,DeleteView, View
from .models import *
from Modulos.Base.models import *
from Modulos.Base.views import consultaDatosEmpresa
from Modulos.AreasTrabajo.models import *
from .forms import *
from django.urls import reverse_lazy
from .serializers import PuestosSerializer
from rest_framework.generics import ListAPIView

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

#Buscador API
class Buscador(ListAPIView):
    serializer_class = PuestosSerializer

    def get_queryset(self):
        search = self.request.GET.get('search','')
        puestos = Puestos.objects.filter(nombre__icontains=search)
        return puestos


#VISTAS DE ADMIN

class PanelListPuestos(ListView):
    model = Puestos
    template_name = 'panel/Puestos/listado.html'
    context_object_name = 'puestos'
    paginate_by = 10
    queryset = Puestos.objects.filter(estatus = True).order_by('nombre')

class PanelCreatePuestos(CreateView):
    model = Puestos
    form_class = PuestosForm
    template_name = 'panel/Puestos/formulario.html'
    success_url = reverse_lazy('Panel:PuestosListar')

class PanelUpdatePuestos(UpdateView):
    model = Puestos
    form_class = PuestosForm
    template_name = 'panel/Puestos/formulario.html'
    success_url = reverse_lazy('Panel:PuestosListar')

class PanelDeletePuestos(DeleteView):
    model = Puestos
    template_name = 'panel/Puestos/eliminar.html'
    success_url = reverse_lazy('Panel:PuestosListar')
