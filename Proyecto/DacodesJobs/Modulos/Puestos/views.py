from django.shortcuts import render, redirect
from django.views.generic import ListView,UpdateView,CreateView,DeleteView, View
from .models import *
from Modulos.Base.models import *
from Modulos.Base.views import consultaDatosEmpresa
from Modulos.AreasTrabajo.models import *
from .forms import *
from django.urls import reverse_lazy
from .serializers import PuestosSerializer
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator

#--------Todos los puestos--------
class PuestosPublicados(ListView):
    def get(self,request,*args,**kwargs):
        puestos = list(Puestos.objects.filter(
            estatus = True,
            disponible = True
        ))

        paginator = Paginator(puestos, 4)
        page = request.GET.get('page')
        puestos = paginator.get_page(page)

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

#--------Puesto publicado--------
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

#--------Buscador API--------
class Buscador(ListAPIView):
    serializer_class = PuestosSerializer

    def get_queryset(self):
        search = self.request.GET.get('search','')
        puestos = Puestos.objects.filter(nombre__icontains=search)
        return puestos

#--------VISTAS DE ADMIN--------
#--------List--------
class PanelListPuestos(ListView):
    model = Puestos
    template_name = 'panel/Puestos/listado.html'
    context_object_name = 'puestos'
    paginate_by = 6
    queryset = Puestos.objects.filter(estatus = True).order_by('nombre')

#--------Create--------
class PanelCreatePuestos(SuccessMessageMixin, CreateView):
    model = Puestos
    form_class = PuestosForm
    template_name = 'panel/Puestos/formulario.html'
    success_message = 'Datos Registrados Exitosamente'
    success_url = reverse_lazy('Panel:PuestosListar')
#--------Update--------
class PanelUpdatePuestos(SuccessMessageMixin, UpdateView):
    model = Puestos
    form_class = PuestosForm
    template_name = 'panel/Puestos/formulario.html'
    success_message = 'Datos Actualizados Exitosamente'
    success_url = reverse_lazy('Panel:PuestosListar')
#--------Delete--------
class PanelDeletePuestos(SuccessMessageMixin, DeleteView):
    model = Puestos
    template_name = 'panel/Puestos/eliminar.html'
    success_message = 'Datos Eliminados Exitosamente'
    success_url = reverse_lazy('Panel:PuestosListar')
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PanelDeletePuestos, self).delete(request, *args, **kwargs)
#--------Export--------
def export_puestos_xls(request):
    from .resources import PuestoResource
    resource = PuestoResource()
    dataset = resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="Puestos publicados.xls"'
    return response
#--------Import--------
def import_puestos_xls(request):
    from .resources import PuestoResource
    from tablib import Dataset
    if request.method == 'POST':
        resource = PuestoResource()
        dataset = Dataset()
        new_puesto = request.FILES['myfile']
        try:
            imported_data = dataset.load(new_puesto.read())
        except:
            messages.warning(request, 'Error, Tipo de archivo no soportado')
            return redirect('Panel:PuestosListar')
        result = resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Importación exitosa')
        else:
            messages.warning(request, 'Error, Verifique que todos los campos del archivo sean correctos')

    return redirect('Panel:PuestosListar')
