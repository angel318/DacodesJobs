from django import forms
from .models import Empleados
from django.contrib.admin import widgets
from django.forms.widgets import *

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ('nombre','apellidos','rfc','imss','nivel_estudios','carrera','direccion','salario','jornada','contrato','fecha_nacimiento','puesto')
        exclude = ('estatus',)
        widgets = {
            'nombre':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese el nombre del empleado','id':'nombre'}),
            'apellidos':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese el apellido del empleado','id':'apellidos'}),
            'rfc':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese el RFC del empleado','id':'rfc'}),
            'imss':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese el numero de seguro social del empleado','id':'imss'}),
            'nivel_estudios':forms.Select(attrs = {'class':'form-control','placeholder':'Ingrese el nivel de estudios del empleado','id':'nivel_estudios'}),
            'direccion':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese la dirección del empleado','id':'direccion'}),
            'carrera':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese la carrera estudiada del empleado','id':'carrera'}),
            'salario':forms.NumberInput(attrs = {'class':'form-control','placeholder':'Ingrese el salario (mensual) del empleado','id':'salario','min':'0.0','value':'0.0'}),
            'jornada':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese la jornada laboral  del empleado','id':'jornada'}),
            'contrato':forms.TextInput(attrs = {'class':'form-control','placeholder':'Ingrese el tipo de contrato del empleado','id':'contrato'}),
            'fecha_nacimiento':DateInput(attrs = {'class':'form-control','id':'datepicker'}),
            'puesto':forms.Select(attrs = {'class':'form-control','id':'puestos'}),
        }
