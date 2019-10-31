from import_export import resources
from .models import Puestos

class PuestoResource(resources.ModelResource):
    class Meta:
     model = Puestos
     exclude = ('imagen_referencial','fecha_creacion','fecha_modificacion','fecha_eliminacion')
