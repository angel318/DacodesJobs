from django import forms
from .models import Candidatos

class CandidatosPostulacionForm(forms.ModelForm):
    class Meta:
        model = Candidatos
        fields = ['nombre','apellidos','telefono','email','curriculum','id_puesto']
        labels = {
            'nombre':'Nombre',
            'curriculum':'Curriculum en PDF',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                    'id':'nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos',
                    'id':'apellidos'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su telefono',
                    'id':'telefono'
                }
            ),
            'id_puesto': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su telefono',
                    'id':'id_puesto'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un correo electrónico',
                    'id':'email'
                }
            ),
            'curriculum': forms.FileInput(
                attrs = {
                    'id':'curriculum'
                }
            ),
        }
