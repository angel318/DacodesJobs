from django import forms
from .models import AreasTrabajo

class AreasForm(forms.ModelForm):
    class Meta:
        model = AreasTrabajo
        fields = ('nombre','jefe','descripcion','imagen_referencial')

        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del área',
                    'id':'nombres'
                }
            ),
            'jefe':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del jefe del área',
                    'id':'jefe'
                }
            ),
            'imagen_referencial': forms.FileInput(
                attrs = {
                    'placeholder':'Ingrese una imagen',
                    'id':'imagen_referencial'
                }
            ),
        }
