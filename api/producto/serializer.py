from rest_framework import serializers
from .models import Producto
from categoria.models import Categoria
from categoria.serializer import CategoriaSerializer

class ProductoSerializer(serializers.ModelSerializer):
    
    id_categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'stock', 'id_categoria']

class ProductoSerializerConCategoria(serializers.ModelSerializer):
    categoria = CategoriaSerializer(source='id_categoria', read_only=True)
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'stock', 'categoria']