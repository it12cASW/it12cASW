from rest_framework import serializers
from polls.models import Issue , Actividad_Issue
from .user_serializer import UserSerializer


class Actividad_IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad_Issue
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    creador = UserSerializer()
    associat = UserSerializer()
    vigilant = UserSerializer(many=True)
    asignada = UserSerializer()
    actividades = Actividad_IssueSerializer(many=True)

    class Meta:
        model = Issue
        fields = ['id', 'asunto', 'descripcion','creador', 'associat', 'asignada','vigilant', 'blocked', 'reason_blocked', 'deadline', 'prioridad', 'status', 'actividades']



    