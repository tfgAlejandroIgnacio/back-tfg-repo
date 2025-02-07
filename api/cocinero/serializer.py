from rest_framework import serializers
from .models import Cocinero

class CocineroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cocinero
        fields = ['id','nombre', 'apellidos', 'correo', 'contraseña']