from django.db import models
from Modulos.AreasTrabajo.models import AreasTrabajo
from Modulos.Base.models import ModeloBase
from django.utils.functional import lazy
from django.core.validators import MinValueValidator, MaxValueValidator

nivel_estudios = [
    ('pri', 'Primaria'),
    ('sec', 'Secundaria'),
    ('bac', 'Bachillerato'),
    ('lic', 'Licenciatura'),
    ('ing', 'Ingeniería '),
    ('mae', 'Maestría'),
    ('doc', 'Doctorado'),
]

class Empleados(ModeloBase):
    nombre = models.CharField('Nombre', max_length = 50)
    apellidos = models.CharField('Apellidos', max_length = 50)
    rfc = models.CharField('RFC', max_length = 13, blank = True)
    imss = models.CharField('Número de seguro social', max_length = 11, blank = False)
    nivel_estudios = models.CharField('Nivel de estudios', max_length = 15, choices = nivel_estudios)
    carrera = models.CharField('Carrera Estudiada',max_length = 50, null = True, blank = True)
    direccion = models.CharField('Dirección', max_length = 100, null = True)
    salario = models.DecimalField('Salario (Mensual)', max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    jornada = models.CharField('Jornada', max_length = 100)
    contrato = models.CharField('Contrato', max_length = 100)
    fecha_nacimiento = models.DateField(null = True)
    fecha_ingreso = models.DateField()
    puesto = models.ForeignKey(AreasTrabajo,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre
