import django_tables2 as tables
from .models import Empleados

class EmpleadosTable(tables.Table):
    class Meta:
        model = Empleados
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id','nombre','salario','jornada','contrato')
        attrs = {"class": "table table-hover table-striped", 'id':'myTable'}
    opciones = tables.TemplateColumn(template_name='panel/Empleados/buttons.html',orderable=False)
