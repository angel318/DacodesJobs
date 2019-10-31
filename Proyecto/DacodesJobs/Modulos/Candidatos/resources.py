from import_export import resources
from .models import Candidatos

class CandidatosResource(resources.ModelResource):
    class Meta:
     model = Candidatos
     exclude = ('fecha_creacion','fecha_modificacion','fecha_eliminacion')
