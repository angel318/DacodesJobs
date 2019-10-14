from django.db import models
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
    id = models.AutoField(primary_key = True)
    estatus = models.BooleanField('Activar / Desactivar', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now = True, auto_now_add = False)
    fecha_eliminacion = models.DateField('Fecha de eliminación', auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class DatosEmpresa(ModeloBase):
    nombre = models.CharField('Nombre', max_length = 50)
    rfc = models.CharField('RFC', max_length = 50, null = True, blank = True, default = 'N/A')
    nosotros = RichTextField()
    telefono = models.CharField('Teléfono', max_length = 20, null = True, blank = True)
    email = models.EmailField('Correo electrónico', max_length = 50, null = True, blank = True)
    direccion = models.CharField('Dirección', max_length = 100, null = True, blank = True)
    twitter = models.CharField('Twitter', max_length = 200, null = True, blank = True)
    facebook = models.CharField('Facebook', max_length = 200, null = True, blank = True)
    instagram = models.CharField('Instagram', max_length = 200, null = True, blank = True)
    linkedin = models.CharField('Linkedin', max_length = 200, null = True, blank = True)
    pagina = models.CharField('Pagina oficial', max_length = 200, null = True, blank = True)

    class Meta:
        verbose_name = 'Datos de la empresa'
        verbose_name_plural = 'Datos de la empresa'

    def __str__(self):
        return self.nombre
