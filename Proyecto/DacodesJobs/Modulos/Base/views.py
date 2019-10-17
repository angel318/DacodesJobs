from django.shortcuts import render,redirect
from django.views.generic import ListView, View, TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy

#MODELOS
from .models import *
from Modulos.Puestos.forms import *
from Modulos.AreasTrabajo.models import *
from Modulos.Empleados.models import *

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from .forms import *

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


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('Panel:Index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsurio(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class PanelListDatosEmpresa(ListView):
    def get(self,request,*args,**kwargs):
        datosEmpresa = consultaDatosEmpresa()

        if datosEmpresa == None:
            datos = {'form' : DatosEmpresaForm,}
            return render(request, 'panel/DatosEmpresa/formulario.html',datos)
        else:
            datos = {'form' : DatosEmpresaForm,'datosEmpresa' : datosEmpresa,}
            return render(request, 'panel/DatosEmpresa/listado.html', datos)

    def post(self,request,*args,**kwargs):
        form = DatosEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Panel:DatosEmpresa')
        else:
            datos = {
                'form':form,
            }
            return render(request,'panel/DatosEmpresa/formulario.html',datos)

class PanelUpdateDatosEmpresa(UpdateView):
    model = DatosEmpresa
    form_class = DatosEmpresaForm
    template_name = 'panel/DatosEmpresa/formulario.html'
    success_url = reverse_lazy('Panel:DatosEmpresa')
