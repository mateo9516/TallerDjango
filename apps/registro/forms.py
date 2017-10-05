from django import forms

from apps.registro.models import Registro

class RegistroForm(forms.ModelForm):

	class Meta:
		model = Registro

		fields = [

			'cantidad_envios_anuales',
			'año',
			'registrante',
			'proveedor',
		]

		labels = {

			'cantidad_envios_anuales': 'Cantidad de Entregas Anuales',
			'año' : 'Año de Entrega',
			'registrante' : 'Nombre del Registrador',
			'proveedor': 'Proveedor',
		}

		widgets = {

			'cantidad_envios_anuales': forms.TextInput(attrs = {'class':'form-control'}),

			'año': forms.TextInput(attrs = {'class':'form-control'}),

			'registrante': forms.TextInput(attrs = {'class':'form-control'}),

			'proveedor': forms.Select(attrs = {'class':'form-control'}), 
		}