from rest_framework import serializers
from .models import *
from django.utils import timezone

 
class UsuarioSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	usuario = serializers.CharField()
	correo = serializers.CharField()
	password = serializers.CharField()

	def create(self,validated_data):
		return Usuario.objects.create(**validated_data)

class AccidenteSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	latitud = serializers.FloatField()
	longitud = serializers.FloatField()
	fecha = serializers.DateField()
	hora = serializers.TimeField()
	usuario = serializers.CharField()

	def create(self,validated_data):
		accidente = Accidente()
		accidente.latitud = validated_data['latitud']
		accidente.longitud = validated_data['longitud']
		accidente.fecha = validated_data['fecha']
		accidente.hora = validated_data['hora']
		accidente.usuario = Usuario.objects.all().get(usuario=validated_data['usuario'])
		accidente.save()
		return accidente	