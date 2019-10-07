from django import forms
from .models import Puestos

class BuscadorForm(forms.ModelForm):
    class Meta:
        model = Puestos
        fields = ('nombre',)
        exclude = ('estado',)

        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                    'id':'puestos'
                }
            ),
        }

class PuestosForm(forms.ModelForm):
    class Meta:
        model = Puestos
        fields = ['disponible','nombre','salario','jornada','contrato','imagen_referencial','descripcion','requisitos','deseable','funciones']
        labels = {
            'nombre':'Nombre del puesto',
            'salario':'Salario del puesto',
            'jornada':'Jornada laboral',
            'contrato':'Tipo de contrato',
            'imagen_referencial':'Imagen de Referencia',
            'descripcion':'Descripción del Puestos',
            'requisitos':'Requisitos del Puesto',
            'deseable':'Aptitudes Deseables',
            'funciones':'Funciones a Desempeñar',
        }
        widgets = {
            'disponible': forms.CheckboxInput(
                attrs = {
                    'class':'custom-control-input',
                    'id':'customSwitch1'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del puesto',
                    'id':'nombre'
                }
            ),
            'salario': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el monto mensual',
                    'id':'salario'
                }
            ),
            'jornada': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el tipo de jornada',
                    'id':'jornada'
                }
            ),
            'contrato': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el tipo de contrato',
                    'id':'contrato'
                }
            ),
            'imagen_referencial': forms.FileInput(
                attrs = {
                    'placeholder':'Ingrese una imagen',
                    'id':'imagen_referencial'
                }
            ),
            'descripcion': forms.TextInput(
                attrs = {
                    'class':'form-control',
                }
            ),
        }
