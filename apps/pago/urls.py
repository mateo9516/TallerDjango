from django.conf.urls import url

from apps.pago.views import indexPago, pagoCreate, pagoList, pagoEdit, pagoDelete

urlpatterns = [
	url(r'^$', indexPago),
	url(r'^nuevo$', pagoCreate.as_view(), name = 'pago_crear'),
	url(r'^listar$', pagoList.as_view(), name = 'pago_listar' ),
	url(r'^editar/(?P<pk>\d+)/$', pagoEdit.as_view(), name='pago_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', pagoDelete.as_view(), name='pago_eliminar'),
]