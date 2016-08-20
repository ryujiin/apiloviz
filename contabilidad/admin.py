from django.contrib import admin
from models import *

class CompraAdmin(admin.ModelAdmin):
	list_display=('id','material','total','fecha')

class StockAdmin(admin.ModelAdmin):
	list_display=('id','material','producto','fecha','operacion','num_operacion','total_acumulado')

admin.site.register(Compra,CompraAdmin)
admin.site.register(Stock,StockAdmin)

# Register your models here.
