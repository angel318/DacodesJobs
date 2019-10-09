from django.db import models
from Modulos.Base.models import ModeloBase
from ckeditor.fields import RichTextField

class Puestos(ModeloBase):
    disponible = models.BooleanField('Disponible', default = False)
    nombre = models.CharField('Nombre del puesto', max_length = 200, null = False, blank = False)
    salario = models.CharField('Salario', max_length = 200, null = False, blank = False)
    jornada = models.CharField('Jornada', max_length = 200, null = False, blank = False)
    contrato = models.CharField('Contrato', max_length = 200, null = False, blank = False)
    imagen_referencial = models.ImageField('Imagen referencial', null = True, blank = True , upload_to = 'Puestos/')
    descripcion = RichTextField()
    requisitos = RichTextField()
    deseable = RichTextField()

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'

    def delete(self, *args, **kwargs):
        self.imagen_referencial.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nombre
