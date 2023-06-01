
from rest_framework.serializers import ModelSerializer
# importa User
from django.contrib.auth.models import User

from rest_framework import serializers
from polls.models import Issue, Actividad_Issue, Equipo, Miembro_Equipo, Imagen_Perfil, Comentario, Watcher, Deadline
from django.contrib.auth.models import User
from . import comment_serializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email','about')


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


class IssueFullSerializer(serializers.ModelSerializer):
    creador = UserSerializer()
    associat = UserSerializer()
    vigilant = UserSerializer(many=True)
    asignada = UserSerializer()

    class Meta:
        model = Issue
        fields = ['id', 'asunto', 'descripcion', 'creador', 'associat', 'vigilant', 'deleted', 'asignada', 'blocked', 'reason_blocked', 'deadline', 'prioridad', 'status']

class Actividad_IssueSerializer(serializers.ModelSerializer):
    issue = IssueFullSerializer()
    creador = UserSerializer()
    usuario = UserSerializer()
    class Meta:
        model = Actividad_Issue
        fields = '__all__'



class EquipoSerializer(serializers.ModelSerializer):
    creador = UserSerializer()

    class Meta:
        model = Equipo
        fields = '__all__'

class UserFullSerializer(serializers.ModelSerializer):
    actividades_hechas = Actividad_IssueSerializer(many=True, read_only=True)
    issues_vigiladas = IssueFullSerializer(many=True)
    comments = ComentarioSerializer(many=True, read_only=True)
    equipos_creados = EquipoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email','about', 'actividades_hechas', 'issues_vigiladas', 'equipos_creados','comments']


        