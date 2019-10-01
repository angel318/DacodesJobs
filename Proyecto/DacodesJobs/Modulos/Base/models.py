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
    nombre = models.CharField('Nombre', max_length = 200)
    nosotros = RichTextField()
    telefono = models.CharField('Teléfono', max_length = 20, null = True, blank = True)
    email = models.EmailField('Correo electrónico', max_length = 200, null = True, blank = True)
    direccion = models.CharField('Dirección', max_length = 200, null = True, blank = True)
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

class Puestos(ModeloBase):
    disponible = models.BooleanField('Disponible', default = True)
    nombre = models.CharField('Nombre del puesto', max_length = 200, null = False, blank = False)
    salario = models.CharField('Salario', max_length = 200, null = False, blank = False)
    jornada = models.CharField('Jornada', max_length = 200, null = False, blank = False)
    contrato = models.CharField('Contrato', max_length = 200, null = False, blank = False)
    imagen_referencial = models.ImageField('Imagen referencial', null = True, blank = True , upload_to = 'Puestos/')
    descripcion = RichTextField()
    requisitos = RichTextField()
    deseable = RichTextField()
    funciones = RichTextField()

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'

    def __str__(self):
        return self.nombre

class AreasTrabajo(ModeloBase):
    nombre = models.CharField('Nombre del area', max_length = 200, null = False, blank = False)
    jefe = models.CharField('Nombre del jefe de area', max_length = 200, null = False, blank = False, default = 'N/A')
    imagen_referencial = models.ImageField('Imagen referencial', null = True, blank = True , upload_to = 'AreasTrabajo/')

    class Meta:
        verbose_name = 'Area de trabajo'
        verbose_name_plural = 'Areas de trabajo'

    def __str__(self):
        return self.nombre

def Categorias():
    puestosArray = []
    try:
        puestos = AreasTrabajo.objects.all().filter(
            estatus = True
        ).values_list('nombre',flat = True)
        for puesto in puestos:
            puestosArray.append((puesto,puesto))
    except:
        puestos = None
    return puestosArray

class Empleados(ModeloBase):
    nombre = models.CharField('Nombre del puesto', max_length = 200, null = False, blank = False)
    direccion = models.CharField('Dirección', max_length = 200, null = True, blank = False)
    salario = models.CharField('Salario (Mensual)', max_length = 200, null = False, blank = False)
    jornada = models.CharField('Jornada', max_length = 200, null = False, blank = False)
    contrato = models.CharField('Contrato', max_length = 200, null = False, blank = False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', max_length = 200, null = True, blank = False)
    puesto = models.CharField('Puesto', max_length=6, choices=Categorias(), default='n/a')

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre
