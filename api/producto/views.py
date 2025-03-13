from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .serializer import ProductoSerializer, ProductoSerializerConCategoria
from .models import Producto

class ProductoSimple(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        listaProductos = ProductoSerializerConCategoria(productos, many=True)
        return Response(listaProductos.data, status=status.HTTP_200_OK)
    def post(self, request):
        datos = ProductoSerializer(data=request.data)
        if datos.is_valid():
            datos.save()
            return Response("Producto almacenado correctamente", status=status.HTTP_201_CREATED)
        else:
            return Response("El producto no se ha almacenado", status=status.HTTP_400_BAD_REQUEST)
        
class ProductoConId(APIView):
    def get(self, request, id):
        try:
            producto = Producto.objects.get(pk=id)
            productoSerializado = ProductoSerializerConCategoria(producto)
            return Response(productoSerializado.data, status=status.HTTP_200_OK)
        except:
            return Response("No se encontró el producto solicitado", status=status.HTTP_404_NOT_FOUND)
                
    def put(self, request, id):
        
        try:
            producto = Producto.objects.get(pk=id)
            productoAModificar = ProductoSerializer(producto, data=request.data)

            if productoAModificar.is_valid():
                productoAModificar.save()
                return Response("Producto modificado correctamente", status=status.HTTP_200_OK)
            else:
                return Response("El producto no pudo ser modificado", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("No se encontró el producto solicitado.", status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id ):
        try:
            producto = Producto.objects.get(pk=id)
            producto.delete()
            return Response("Producto modificado correctamente", status=status.HTTP_200_OK)
        except:
            return Response("No se encontró el producto solicitado", status=status.HTTP_404_NOT_FOUND)    