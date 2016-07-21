from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser

#Viewset para busquedas
from drf_haystack.viewsets import HaystackViewSet

from models import *

#Importar serializadeores
from serializers import *

class ProductoBusquedaViewSet(HaystackViewSet):
    index_models = [Producto]
    serializer_class = ProductoBusquedaSerializer

class CategoriaViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = CategoriaSerializer
	queryset = Categoria.objects.all()

class ProductoListaViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = ProductoListaSerializer
	queryset = Producto.objects.all()