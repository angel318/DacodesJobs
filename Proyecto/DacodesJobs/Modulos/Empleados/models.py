from django.db import models
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Base.models import ModeloBase

# Create your models here.
def AreasDeTrabajo():
    areasArray = []
    try:
        areas = AreasTrabajo.objects.all().filter(
            estatus = True
        ).values_list('nombre',flat = True)
        for area in areas:
            areasArray.append((area,area))
    except:
        areas = None
    return areasArray

class Empleados(ModeloBase):
    nombre = models.CharField('Nombre del puesto', max_length = 200, null = False, blank = False)
    direccion = models.CharField('Dirección', max_length = 200, null = True, blank = False)
    salario = models.CharField('Salario (Mensual)', max_length = 200, null = False, blank = False)
    jornada = models.CharField('Jornada', max_length = 200, null = False, blank = False)
    contrato = models.CharField('Contrato', max_length = 200, null = False, blank = False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', max_length = 200, null = True, blank = False)
    puesto = models.CharField('Puesto', max_length=6, choices=AreasDeTrabajo(), default='n/a')

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre
