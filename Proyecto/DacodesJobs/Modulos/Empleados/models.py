from django.db import models
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Base.models import ModeloBase
from django.utils.functional import lazy

class Empleados(ModeloBase):
    nombre = models.CharField('Nombre del empleado', max_length = 200, null = False, blank = False)
    direccion = models.CharField('Dirección', max_length = 200, null = True, blank = False)
    salario = models.CharField('Salario (Mensual)', max_length = 200, null = False, blank = False)
    jornada = models.CharField('Jornada', max_length = 200, null = False, blank = False)
    contrato = models.CharField('Contrato', max_length = 200, null = False, blank = False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', max_length = 200, null = True, blank = False)
    puesto = models.ForeignKey(AreasTrabajo,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre
