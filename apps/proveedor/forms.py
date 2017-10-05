from django import forms

from apps.proveedor.models import Proveedor

class ProveedorForm(forms.ModelForm):

	class Meta:
		model = Proveedor

		fields = [

			'nombre',
			'apellidos',
			'cedula',
			'matricula',
			'telefono',
		]

		labels = {

			'nombre': 'Nombre',
			'apellidos' : 'Apellidos',
			'cedula' : 'Cédula',
			'matricula': 'Matrícula',
			'telefono': 'Teléfono',
		}

		widgets = {

			'nombre': forms.TextInput(attrs = {'class':'form-control'}),

			'apellidos': forms.TextInput(attrs = {'class':'form-control'}),

			'cedula': forms.TextInput(attrs = {'class':'form-control'}),

			'matricula': forms.TextInput(attrs = {'class':'form-control'}),

			'telefono': forms.TextInput(attrs = {'class':'form-control'}),
	 
		}