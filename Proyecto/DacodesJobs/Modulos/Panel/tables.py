import django_tables2 as tables
from django.contrib.auth.models import User

class EmpleadosTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ('username','first_name','last_name','email')
        attrs = {"class": "table table-hover table-striped", 'id':'myTable'}
    opciones = tables.TemplateColumn(template_name='panel/User/buttons.html',orderable=False)
