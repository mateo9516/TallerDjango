from django.db import models

from apps.proveedor.models import Proveedor

# Create your models here.

class Registro(models.Model):

	cantidad_envios_anuales = models.CharField(max_length = 50)
	año = models.IntegerField()
	registrante = models.CharField(max_length = 70)
    
	proveedor = models.ForeignKey(Proveedor, null = True, blank = False, on_delete = models.CASCADE)
