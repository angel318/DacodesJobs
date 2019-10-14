from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import DatosEmpresa

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class DatosEmpresaForm(forms.ModelForm):
    class Meta:
        model = DatosEmpresa
        fields = ('nombre','rfc','nosotros','telefono','email','direccion','twitter','facebook','instagram','linkedin','pagina')

        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del empleado',
                    'id':'puestos'
                }
            ),
            'rfc':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el rfc',
                    'id':'rfc'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono',
                    'id':'telefono'
                }
            ),
            'email':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un email de contacto',
                    'id':'email'
                }
            ),
            'direccion':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la dirección de la empresa',
                    'id':'direccion'
                }
            ),
            'twitter':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el twitter de la empresa',
                    'id':'twitter'
                }
            ),
            'facebook':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el facebook de la empresa',
                    'id':'facebook'
                }
            ),
            'instagram':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el instagram de la empresa',
                    'id':'instagram'
                }
            ),
            'linkedin':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el linkedin de la empresa',
                    'id':'linkedin'
                }
            ),
            'pagina':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el pagina de la empresa',
                    'id':'pagina'
                }
            ),
        }
