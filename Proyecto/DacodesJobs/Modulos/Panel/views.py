from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView, View, ListView
from Modulos.Empleados.models import Empleados
from Modulos.Candidatos.models import Candidatos
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Puestos.models import Puestos
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages

def grafica3(query3):
    grafica3 = {}
    for graf in query3:
        areaTrabajo = AreasTrabajo.objects.filter(id = graf[0]).get()
        grafica3[areaTrabajo.nombre] = Empleados.objects.filter(puesto = graf).count()
    return grafica3

def grafica2(query2):
    grafica2 = {}
    for graf in query2:
        puestoCandidato = Puestos.objects.filter(id = graf[0]).get()
        grafica2[puestoCandidato.nombre] = Candidatos.objects.filter(id_puesto = graf[0]).count()
    return grafica2

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
        usuariosCount = User.objects.count()


        query1 = Empleados.objects.values_list('nivel_estudios','id').distinct()
        query2 = Candidatos.objects.values_list('id_puesto').distinct()
        query3 = Empleados.objects.values_list('puesto_id').distinct()
        print(query2)

        datos = {
            'topEmpleados' : topEmpleados,
            'empleadosCount' : empleadosCount,
            'candidatosCount' : candidatosCount,
            'usuariosCount' : usuariosCount,
            'areasCount' : areasCount,
            'puestosCount' : puestosCount,
            'grafica1' :grafica1(query1),
            'grafica2' :grafica2(query2),
            'grafica3' :grafica3(query3),
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
            messages.success(request, 'Actualización Realizada.')
            datos = {
                'usuario' : usuario
            }
            return redirect('Panel:UsuarioConfig')
        else:
            datos = {
                'form':form,
            }
            return render(request,'panel/User/formulario.html',datos)

class PanelListUsuarios(ListView):
    model = User
    template_name = 'panel/User/listado.html'
    context_object_name = 'users'
    paginate_by = 10
    def get_queryset(self):
        queryset = User.objects.order_by('username').exclude(username = self.request.user.username).all()
        #queryset = User.objects.order_by('username').all()
        return queryset
