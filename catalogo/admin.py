from django.contrib import admin
from models import *

class ProductoImagenInline(admin.TabularInline):
	model = ProductoImagen

class VariacionInline(admin.TabularInline):
	model = ProductoVariacion

class ProductoAdmin(admin.ModelAdmin):
	inlines = [ProductoImagenInline,VariacionInline,]
	filter_horizontal = ('relaciones','categorias')
	list_display = ('id','foto_producto','full_name','nombre','slug','activo')

	def foto_producto(self, obj):
		url = obj.get_thum()
		tag = None
		if url:
			url = url.url
			tag = '<img src="%s" width="50">' % url
		return tag
	foto_producto.allow_tags = True

class CategoriaAdmin(admin.ModelAdmin):
	list_display=('nombre','full_name','slug','nombre')

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Material)
