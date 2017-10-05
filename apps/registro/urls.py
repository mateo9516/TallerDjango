from django.conf.urls import url , include

from apps.registro.views import registro_view, registroList, registroDelete, registroCreate, registroEdit

urlpatterns = [
	url(r'^$', registro_view),
	url(r'^nuevo$', registroCreate.as_view(), name = 'registro_crear'),
	url(r'^listar$', registroList.as_view(), name = 'registro_listar' ),
	url(r'^editar/(?P<pk>\d+)/$', registroEdit.as_view(), name='registro_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', registroDelete.as_view(), name='registro_eliminar'),
	
]