from rest_framework import serializers
from models import *

#Serializer para la busqueda
from drf_haystack.serializers import HaystackSerializer, HighlighterMixin
from search_indexes import ProductoIndex

class ProductoBusquedaSerializer(HighlighterMixin, HaystackSerializer):
	highlighter_html_tag = "em"
	class Meta:
		index_classes = [ProductoIndex]
		fields = ['full_name',]

class CategoriaSerializer(serializers.ModelSerializer):
	padre = serializers.CharField(read_only=True)
	link  = serializers.SerializerMethodField()
	imagen = serializers.SerializerMethodField()
	class Meta:
		model = Categoria
		fields = ('id','nombre','full_name','seccion','slug','descripcion','activo','imagen','padre','link','titulo_seo')

	def get_link(self,obj):
		link = '/catalogo/%s/' %obj.slug
		return link

	def get_imagen(self,obj):
		if obj.imagen:
			return obj.imagen.url
		else:
			return None

class ProductoListaSerializer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField()

	class Meta:
		model = Producto
		fields=['id','nombre','full_name','slug','thum']

	def get_thum(self,obj):
		url = None
		if obj.get_thum():
			url = obj.get_thum().url
		return url
