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
