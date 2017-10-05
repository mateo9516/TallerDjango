from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.pago.forms import PagoForm
from apps.pago.models import Pago

#Create your views here

def indexPago(request):
	return render(request, 'pago/index.html')

class pagoList(ListView):
	model = Pago
	template_name = 'pago/pago_list.html'

class pagoDelete(DeleteView):
	model = Pago
	template_name = 'pago/pago_delete.html'
	success_url = reverse_lazy('Pago:pago_listar')

class pagoEdit(UpdateView):
	model = Pago
	fields = '__all__'
	template_name = 'pago/pago_crear.html'
	success_url = reverse_lazy('Pago:pago_listar')

class pagoCreate(CreateView):
	model = Pago
	fields = '__all__'
	template_name = 'pago/pago_crear.html'	
	success_url = reverse_lazy('Pago:pago_listar')	