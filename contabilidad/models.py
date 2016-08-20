from __future__ import unicode_literals

from django.db import models
from catalogo.models import Material,ProductoVariacion

# Create your models here.
class Compra(models.Model):
	material = models.ForeignKey(Material,blank=True)
	slug = models.CharField(max_length=100,blank=True,unique=True,editable=False)
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	cantidad = models.PositiveIntegerField(default=0)
	fecha = models.DateTimeField(auto_now=True)
	total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,editable=False)
	operacion_stock = models.ForeignKey('Stock',blank=True,null=True)

	def save(self, *args, **kwargs):
		self.slug = self.get_slug();
		self.total = self.precio * self.cantidad
		nuevo_stock = Stock(material = self.material ,operacion = 'mas',num_operacion=self.slug,total = self.cantidad,ultimo_precio=self.precio)
		nuevo_stock.save()		
		self.operacion_stock = nuevo_stock
		super(Compra, self).save(*args, **kwargs) 

	def get_slug(self):
		operacion = Compra.objects.all().count() + 1
		slug = '%s%s-%s-C' %(self.material.id,self.material.nombre[0],operacion)
		return slug

class Stock(models.Model):
	OPERACIONES=(
		('mas','Aumenta'),
		('menos','Disminuye')
		)
	material = models.ForeignKey(Material,blank=True,null=True)
	producto = models.ForeignKey(ProductoVariacion,blank=True,null=True)
	fecha = models.DateTimeField(auto_now=True)
	operacion = models.CharField(max_length=10,choices=OPERACIONES)
	num_operacion = models.CharField(max_length=100,blank=True,editable=False)
	total = models.IntegerField(default=0)
	total_acumulado = models.IntegerField(default=0)
	ultimo_precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

	def save(self, *args, **kwargs):
		self.total_acumulado = self.get_total_acumulado()
		super(Stock, self).save(*args, **kwargs)

	def get_total_acumulado(self):
		total = 0
		if self.material:
			totales = Stock.objects.filter(material = self.material).order_by('-fecha')[:1]
		elif self.producto:
			totales = Stock.objects.filter(producto = self.producto).order_by('-fecha')[:1]
		
		if totales:
			total = totales[0].total_acumulado + self.total
		else:
			total = 0 + self.total

		if self.operacion == 'mas':
			total = total + self.total
		else:
			total = total - self.total
		return total