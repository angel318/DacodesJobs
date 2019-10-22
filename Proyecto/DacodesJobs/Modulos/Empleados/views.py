from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import EmpleadosForm
from django.urls import reverse_lazy
from django.http import HttpResponse

class PanelListEmpleados(ListView):
    model = Empleados
    template_name = 'panel/Empleados/listado.html'
    context_object_name = 'empleados'
    paginate_by = 10
    queryset = Empleados.objects.filter(estatus = True).order_by('nombre')

class PanelCreateEmpleados(CreateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'panel/Empleados/formulario.html'
    success_url = reverse_lazy('Panel:EmpleadosListar')

class PanelUpdateEmpleados(UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'panel/Empleados/formulario.html'
    success_url = reverse_lazy('Panel:EmpleadosListar')

class PanelDeleteEmpleados(DeleteView):
    model = Empleados
    template_name = 'panel/Empleados/eliminar.html'
    success_url = reverse_lazy('Panel:EmpleadosListar')

def export_empleados_xls(request):
    from .resources import EmpleadosResource
    resource = EmpleadosResource()
    dataset = resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="Empleados.xls"'
    return response

def import_empleados_xls(request):
    from .resources import EmpleadosResource
    from tablib import Dataset
    from django.contrib import messages
    if request.method == 'POST':
        resource = EmpleadosResource()
        dataset = Dataset()
        new_empleado = request.FILES['myfile']
        imported_data = dataset.load(new_empleado.read())
        result = resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Importacion exitosa')
        else:
            messages.warning(request, 'Error, Verifique que todos los campos sean correctos')

    return redirect('Panel:EmpleadosListar')
