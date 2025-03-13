from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .serializer import CategoriaSerializer
from .models import Categoria

class CategoriaSimple(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        categoriasSerializadas = CategoriaSerializer(categorias, many=True)
        return Response(categoriasSerializadas.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        datos_categoria = CategoriaSerializer(data=request.data)
        if datos_categoria.is_valid():
            datos_categoria.save()
            return Response("Categoria guardada correctamente", status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class CategoriaConId(APIView):
    def get(self, request, id):
        try:
            categoria = Categoria.objects.get(pk=id)
        except ObjectDoesNotExist:
            return Response("Categoria no encontrada",status=status.HTTP_404_NOT_FOUND)
        categoriaSerializer = CategoriaSerializer(categoria)    
        return Response(categoriaSerializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        try:
            categoria = Categoria.objects.get(pk=id)
            categoria.delete()
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response("Categoria no encontrada",status=status.HTTP_404_NOT_FOUND) 