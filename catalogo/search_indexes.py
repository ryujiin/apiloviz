import datetime
from haystack import indexes
from models import Producto

class ProductoIndex(indexes.SearchIndex,indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	full_name = indexes.CharField(model_attr="full_name")	
	creado = indexes.DateTimeField(model_attr="creado")

	def get_model(self):
		return Producto

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(creado__lte=datetime.datetime.now())