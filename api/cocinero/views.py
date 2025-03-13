from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import Cocinero
from .serializer import CocineroSerializer

class CocineroSimple(APIView):
    def get(self, request):
        cocineros = Cocinero.objects.all()
        listaCocineros = CocineroSerializer(cocineros, many=True)
        return Response(listaCocineros.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        cocinero = CocineroSerializer(data=request.data)
        if cocinero.is_valid():
            cocinero.save()
            return Response(cocinero.data, status=status.HTTP_201_CREATED)
        return Response(cocinero.errors, status=status.HTTP_400_BAD_REQUEST)

class CocineroComplejo(APIView):
    def get(self, request, id):
        try:
            cocinero = Cocinero.objects.get(pk=id)
            cocineroSerializado = CocineroSerializer(cocinero)
            return Response(cocineroSerializado.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Cocinero no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            cocinero = Cocinero.objects.get(pk=id)
            cocinero.delete()
            return Response({"mensaje": "Cocinero eliminado correctamente"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Cocinero no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            cocinero = Cocinero.objects.get(pk=id) 
            cocineroSerializado = CocineroSerializer(cocinero, data=request.data)
            if cocineroSerializado.is_valid():
                cocineroSerializado.save()
                return Response(cocineroSerializado.data, status=status.HTTP_200_OK)
            return Response(cocineroSerializado.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error": "Cocinero no encontrado"}, status=status.HTTP_404_NOT_FOUND)
