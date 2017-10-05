from django.conf.urls import url, include

from apps.proveedor.views import indexProveedor, proveedorList, proveedorDelete, proveedorCreate, proveedorEdit

urlpatterns = [
	url(r'^$', indexProveedor),
	url(r'^nuevo$', proveedorCreate.as_view(), name = 'proveedor_crear'),
	url(r'^listar$', proveedorList.as_view(), name = 'proveedor_listar' ),
	url(r'^editar/(?P<pk>\d+)/$', proveedorEdit.as_view(), name='proveedor_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', proveedorDelete.as_view(), name='proveedor_eliminar'),
]