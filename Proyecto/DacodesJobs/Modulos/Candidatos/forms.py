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

class CorreoForm(forms.Form):
    asunto=forms.CharField(required=True)
    destino=forms.EmailField()
    contenido=forms.CharField(max_length=999, widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asunto'].widget.attrs['class'] = 'form-control' 
        self.fields['destino'].widget.attrs['class'] = 'form-control'
        self.fields['contenido'].widget.attrs['class'] = 'form-control'
