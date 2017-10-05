from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.proveedor.forms import ProveedorForm
from apps.proveedor.models import Proveedor

#Create your views here

def indexProveedor(request):
	return render(request, 'proveedor/index.html')


class proveedorList(ListView):
	model = Proveedor
	template_name = 'proveedor/proveedor_list.html'

class proveedorDelete(DeleteView):
	model = Proveedor
	template_name = 'proveedor/proveedor_delete.html'
	success_url = reverse_lazy('Proveedor:proveedor_listar')

class proveedorEdit(UpdateView):
	model = Proveedor
	fields = '__all__'
	template_name = 'proveedor/proveedor_crear.html'
	success_url = reverse_lazy('Proveedor:proveedor_listar')

class proveedorCreate(CreateView):
	model = Proveedor
	fields = '__all__'
	template_name = 'proveedor/proveedor_crear.html'	
	success_url = reverse_lazy('Proveedor:proveedor_listar')		
