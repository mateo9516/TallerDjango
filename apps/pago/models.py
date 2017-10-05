from django.db import models

# Create your models here.

from apps.proveedor.models import Proveedor

class Pago(models.Model):
	
	tipoPago = models.CharField(max_length = 20)
	proveedor = models.ForeignKey(Proveedor, null = True, blank = False, on_delete = models.CASCADE)	
