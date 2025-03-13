from rest_framework import serializers
from .models import Cocinero
from django.contrib.auth.hashers import make_password

class CocineroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cocinero
        fields = ['id','nombre', 'apellidos', 'correo']

class CocineroSerializerConContraseña(serializers.ModelSerializer):
    class Meta:
        model = Cocinero
        fields = ['id','nombre','apellidos','correo','contraseña']    

    def create(self, validated_data):
        validated_data['contraseña'] = make_password(validated_data['contraseña'])  # Hashea antes de guardar
        return super().create(validated_data)   

    def update(self, instance, validated_data):
        if 'contraseña' in validated_data:
            validated_data['contraseña'] = make_password(validated_data['contraseña'])  # Hashea si se actualiza
        return super().update(instance, validated_data)    
     