"""apiloviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

import settings

from rest_framework.routers import DefaultRouter
from catalogo.views import *
from cliente.views import *
from carro.views import *
from cms.views import *
from utiles.views import *
from pedido.views import *
from ubigeo.views import *

router = DefaultRouter()

#router.register(r'productoLista', ProductoListaViewsets,'producto lista')

router.register(r'producto/lista', ProductoListaViewsets,'productos Lista')
router.register(r'producto/single', ProductoSingleViewsets,'productos single')
router.register(r'categoria', CategoriaViewsets,'categorias')


router.register(r'carro/lineas',LineasViewsets,'lineas')
router.register(r'cmsweb/carrusel',CarruselViewsets,'carruseles')
router.register(r'cmsweb/pages',PageViewsets,'pages')
router.register(r'cmsweb/menus',MenuViewsets,'menus')
router.register(r'colores',ColorViewsets,'coleres')
router.register(r'tallas',TallasViewsets,'tallas')
router.register(r'pedidos',PedidoViewSet,'pedidos')
router.register(r'ubigeo',RegionViewset,'ubigeo')
router.register(r'cliente/direcciones',DireccionViewsets,'direcciones')
router.register(r'metodos_envio',MetodoEnvioViewSet,'mentodos_envios')
router.register(r'comentarios',ComentarioViewSet,'comentarios')
router.register(r'comentarioimgs',ComentarioImagenViewSet,'comentarios_imagenes')
router.register(r'cliente/suscrito',SuscritoViewset,'suscritos')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
    url(r'^api/user/perfil/$',PerfilUserViewSet.as_view(),name='prefil_user'),
    url(r'^api/carro/', include('carro.urls')),    
    url(r'^',include('cms.urls')),
]
if settings.DEBUG:
    urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
] + urlpatterns