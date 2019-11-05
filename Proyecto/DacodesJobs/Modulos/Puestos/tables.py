import django_tables2 as tables
from .models import Puestos

class EmpleadosTable(tables.Table):
    class Meta:
        model = Puestos
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id','nombre','salario','contrato')
        attrs = {"class": "table table-hover table-striped", 'id':'myTable'}
    estatus = tables.TemplateColumn(template_name='panel/Puestos/estatus.html',orderable=False)
    opciones = tables.TemplateColumn(template_name='panel/Puestos/buttons.html',orderable=False)
