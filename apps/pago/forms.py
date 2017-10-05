from django import forms

from apps.pago.models import Pago

class PagoForm(forms.ModelForm):

	class Meta:
		model = Pago

		fields = [

			'tipoPago',
			'proveedor',
			
		]

		labels = {

			'tipoPago': 'Tipo Pago',
			'proveedor' : 'Proveedor',
			
		}

		widgets = {

			'tipoPago': forms.TextInput(attrs = {'class':'form-control'}),

			'proveedor': forms.Select(attrs = {'class':'form-control'}),

			
	 
		}