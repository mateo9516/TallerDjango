from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.registro.forms import RegistroForm
from apps.registro.models import Registro 
#Create your views here

def registro_view(request):
	return render(request, 'registro/index.html')


class registroList(ListView):
	model = Registro
	template_name = 'registro/registro_list.html'

class registroDelete(DeleteView):
	model = Registro
	template_name = 'registro/registro_delete.html'
	success_url = reverse_lazy('Registro:registro_listar')

class registroEdit(UpdateView):
	model = Registro
	fields = '__all__'
	template_name = 'registro/registro_form.html'
	success_url = reverse_lazy('Registro:registro_listar')

class registroCreate(CreateView):
	model = Registro
	fields = '__all__'
	template_name = 'registro/registro_form.html'	
	success_url = reverse_lazy('Registro:registro_listar')	