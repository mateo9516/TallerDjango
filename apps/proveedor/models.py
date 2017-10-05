from django.db import models

# Create your models here.

class Proveedor(models.Model):

	nombre = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 70)
	cedula = models.IntegerField()
	matricula = models.CharField(max_length = 10)
	telefono = models.IntegerField()
 	
	def __str__(self):
 		return '{} {} {}'.format(self.nombre , self.apellidos , self.cedula)	