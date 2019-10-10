from django.db import models
from Modulos.Base.models import ModeloBase
from Modulos.Puestos.models import Puestos
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

# Create your models here.
class Candidatos(ModeloBase):
    id_puesto = models.ForeignKey(Puestos,on_delete=models.CASCADE)
    nombre = models.CharField('Nombre del candidato', max_length = 50, null = False, blank = False)
    apellidos = models.CharField('Apellidos', max_length = 50, null = False, blank = False)
    telefono = models.CharField('Teléfono', max_length = 20, null = True, blank = True)
    email = models.EmailField('Correo electrónico', max_length = 200, null = True, blank = True)
    curriculum = models.FileField('Curriculum', null = True, blank = True , upload_to = 'Candidatos/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def delete(self, *args, **kwargs):
        self.curriculum.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nombre
