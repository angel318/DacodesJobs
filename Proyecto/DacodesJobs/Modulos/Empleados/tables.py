from django_tables2 import tables, TemplateColumn
from .models import Empleados
import django_tables2 as tables
import itertools

class EmpleadosTable(tables.Table):
    salario = tables.Column(footer="Total:") 
    class Meta:
        model = Empleados
        fields = ('id','nombre','salario','jornada','contrato')
        attrs = {'class': 'table table-striped table-hover text-center'}
    opciones = TemplateColumn(template_name='panel/Empleados/buttons.html',orderable=False)
