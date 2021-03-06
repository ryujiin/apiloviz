from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from models import *
from serializers import *

from datetime import datetime, timedelta, time

how_many_days = 20

class ProductoListaViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = ProductoListaSerializer
	
	def get_queryset(self):
		queryset = Producto.objects.filter(activo=True).order_by('-actualizado')
		return queryset


#vista a remplazar
class ProductoSingleViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = ProductoSingleSereializer
	
	def get_queryset(self):
		queryset = Producto.objects.filter(activo=True).order_by('-actualizado')
		return queryset

# Create your views here.
class CategoriaViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = CategoriaSerializer
	queryset = Categoria.objects.all()


#Vistas para la oficina
class ProductosOficinaViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = ProductoListaSerializer
	permission_classes = (IsAdminUser,)

	def get_queryset(self):
		queryset = Producto.objects.filter(activo=True).order_by('-pk')
		return queryset

class ProductoSingleEditableViewsets(viewsets.ModelViewSet):
	serializer_class = ProductoSingleEditable
	permission_classes = (IsAdminUser,)

	def get_queryset(self):
		queryset = Producto.objects.all().order_by('-pk')
		return queryset
