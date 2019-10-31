from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView
from Modulos.Empleados.models import Empleados
from Modulos.Candidatos.models import Candidatos
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Puestos.models import Puestos
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

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

def grafica4(query4):
    grafica4 = {}
    for graf in query4:
        grafica4[graf[0]] = Empleados.objects.filter(salario = graf[0]).count()
    return grafica4

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
        query4 = Empleados.objects.values_list('salario').distinct()
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
            'grafica4' :grafica4(query4),
        }
        return render(request, 'panel/index.html', datos)

class PanelUsuarioConfig(TemplateView):
    template_name = 'panel/User/formulario.html'

    def post(self,request,*args,**kwargs):
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Actualización Realizada.')
            return redirect('Panel:UsuarioConfig')
        else:
            datos = {'form':form,}
            return render(request,'panel/User/formulario.html',datos)

class PanelUsuarioChangePassword(TemplateView):
    template_name = 'panel/User/change_password.html'

    def post(self, request,*args,**kwargs):
        from django.contrib.auth.forms import PasswordChangeForm
        from django.contrib.auth import update_session_auth_hash

        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            print(form.cleaned_data["new_password1"])
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Contraseña Cambiada Con Éxito.')
            return redirect('Panel:UsuarioConfig')
        else:
            messages.warning(request, ('Hubo algunos errores en la información que ingresó. Por favor, corrija lo siguiente:'))
            datos = {'form':form}
            return render(request,'panel/User/change_password.html',datos)

class PanelListUsuarios(ListView):
    model = User
    template_name = 'panel/User/listado.html'
    context_object_name = 'users'
    paginate_by = 10
    def get_queryset(self):
        queryset = User.objects.order_by('username').exclude(username = self.request.user.username).all()
        return queryset

class PanelCreateUsuario(SuccessMessageMixin, CreateView):
    model = UserForm
    template_name = 'panel/User/formulario_crear.html'
    form_class = UserCreateForm
    success_message = 'Datos Registrados Exitosamente'
    success_url = reverse_lazy('Panel:UsuariosListar')
