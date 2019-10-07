from django import forms
from .models import Empleados

class DateInput(forms.DateInput):
    input_type = 'date'

class ExampleForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ('nombre','direccion','salario','jornada','contrato','fecha_nacimiento','puesto')
        exclude = ('estatus',)

        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del empleado',
                    'id':'puestos'
                }
            ),
            'direccion':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la dirección del empleado',
                    'id':'direccion'
                }
            ),
            'salario':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el salario (mensual) del empleado',
                    'id':'salario'
                }
            ),
            'jornada':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la jornada laboral  del empleado',
                    'id':'jornada'
                }
            ),
            'contrato':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el tipo de contrato del empleado',
                    'id':'contrato'
                }
            ),
            'fecha_nacimiento':DateInput(
                attrs={
                'class':'form-control',
                'id':'fecha_nacimiento'
                }
            ),
            'puesto':forms.Select(
                attrs = {
                    'class':'form-control',
                    'id':'puestos'
                }
            ),
        }
