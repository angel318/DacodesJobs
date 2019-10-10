from django.db import models
from Modulos.Base.models import ModeloBase
from ckeditor.fields import RichTextField

# Create your models here.
class AreasTrabajo(ModeloBase):
    nombre = models.CharField('Nombre del area', max_length = 200, null = False, blank = False)
    jefe = models.CharField('Nombre del jefe de area', max_length = 200, null = False, blank = False, default = 'N/A')
    descripcion = RichTextField()
    imagen_referencial = models.ImageField('Imagen referencial', null = True, blank = True , upload_to = 'AreasTrabajo/')

    class Meta:
        verbose_name = 'Area de trabajo'
        verbose_name_plural = 'Areas de trabajo'

    def delete(self, *args, **kwargs):
        self.imagen_referencial.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nombre
