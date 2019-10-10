from rest_framework import serializers
from .models import Puestos

class PuestosSerializer(serializers.ModelSerializer):
    class Meta():
        model = Puestos
        fields = (
            'nombre',
        )
