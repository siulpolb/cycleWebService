from rest_framework import serializers
from .models import Usuario
 
class UsuarioSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	usuario = serializers.CharField()
	correo = serializers.CharField()
	password = serializers.CharField()

	def create(self,validated_data):
		return Usuario.objects.create(**validated_data)