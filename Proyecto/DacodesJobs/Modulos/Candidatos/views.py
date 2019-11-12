from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView,CreateView,View
from .models import *
from .forms import *
from Modulos.Puestos.models import Puestos
from django.urls import reverse_lazy
from .resources import CandidatosResource
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage

class PanelListCandidatos(ListView):
    model = Candidatos
    template_name = 'panel/Candidatos/listado.html'
    context_object_name = 'candidatos'
    paginate_by = 10
    queryset = Candidatos.objects.filter(estatus = True).order_by('nombre')

class PanelDeleteCandidatos(DeleteView):
    model = Candidatos
    template_name = 'panel/Candidatos/eliminar.html'
    success_url = reverse_lazy('Panel:CandidatosListar')

class Candidatos(CreateView):
    model = Candidatos
    def get(self, request, pk, *args, **kwargs):
        puesto = Puestos.objects.filter(id = pk).get()
        datos = {
            'form': CandidatosPostulacionForm,
            'puesto' : puesto,
        }
        return render(request, 'users/formulario_candidatos.html',datos)

    def post(self, request, pk, *args, **kwargs):
        form = CandidatosPostulacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Puestos:Puestos')
        else:
            datos = {
                'form':form,
            }
            return render(request, 'users/formulario_candidatos.html',datos)

def export_candidatos_xls(request):
    from .resources import CandidatosResource
    resource = CandidatosResource()
    dataset = resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="Candidatos.xls"'
    return response

class PanelMessageCandidatos(View):
    def get(self,request,*args,**kwargs):
        datos = {
            'form': CorreoForm
        }
        return render(request, 'panel/Candidatos/formulario_correo.html',datos)

    def post(self,request,*args,**kwargs):
        form = CorreoForm(request.POST)
        if form.is_valid():
            destino = form.cleaned_data['destino']
            email = EmailMessage('Subject', 'Body', to=[destino])
            email.send()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'panel/Candidatos/formulario_correo.html')
