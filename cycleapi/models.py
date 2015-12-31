from django.db import models

class Usuario(models.Model):
	usuario = models.TextField(max_length=15, unique=True)
	correo = models.TextField(max_length=50,unique=True)
	password = models.TextField(max_length=20)
	m2xDevice = models.TextField(max_length= 100)

	def __unicode__(self):
		return self.usuario

class Accidente(models.Model):
	latitud = models.FloatField()
	longitud = models.FloatField()
	fecha = models.DateField()
	hora = models.TimeField()
	usuario = models.ForeignKey(Usuario, related_name='accidentes')
