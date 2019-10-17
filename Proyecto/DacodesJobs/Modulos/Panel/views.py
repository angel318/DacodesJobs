from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from Modulos.Empleados.models import Empleados
from Modulos.Candidatos.models import Candidatos
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Puestos.models import Puestos
from .forms import *
from django.urls import reverse_lazy

def grafica3(query3):
    grafica3 = {}
    for graf in query3:
        areaTrabajo = AreasTrabajo.objects.filter(id = graf[0]).get()
        grafica3[areaTrabajo.nombre] = Empleados.objects.filter(puesto = graf).count()
    return grafica3

def grafica1(query1):
    grafica1 = {}
    for graf in query1:
        empleado = Empleados.objects.filter(id = graf[1]).get()
        grafica1[empleado.get_nivel_estudios_display()] = Empleados.objects.filter(nivel_estudios = graf[0]).count()
    return grafica1


#Vistas
class PanelIndex(TemplateView):
    def get(self,request,*args,**kwargs):

        topEmpleados = list(Empleados.objects.order_by('-salario'))[:10]
        empleadosCount = Empleados.objects.count()
        candidatosCount = Candidatos.objects.count()
        areasCount = AreasTrabajo.objects.count()
        puestosCount = Puestos.objects.count()

        query3 = Empleados.objects.values_list('puesto_id').distinct()
        query1 = Empleados.objects.values_list('nivel_estudios','id').distinct()

        datos = {
            'topEmpleados' : topEmpleados,
            'empleadosCount' : empleadosCount,
            'candidatosCount' : candidatosCount,
            'areasCount' : areasCount,
            'puestosCount' : puestosCount,
            'grafica3' :grafica3(query3),
            'grafica1' :grafica1(query1),
        }
        return render(request, 'panel/index.html', datos)

class PanelUsuarioConfig(UpdateView):
    def get(self,request,*args,**kwargs):
        usuario = User.objects.filter(username = request.user.username).get()
        datos = {
            'usuario' : usuario
        }
        return render(request, 'panel/User/formulario.html', datos)

    def post(self,request,*args,**kwargs):
        usuario = User.objects.filter(username = request.user.username).get()
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            datos = {
                'usuario' : usuario
            }
            return redirect('Panel:UsuarioConfig')
        else:
            datos = {
                'form':form,
            }
            return render(request,'panel/User/formulario.html',datos)
