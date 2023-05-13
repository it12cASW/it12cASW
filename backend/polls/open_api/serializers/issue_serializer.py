from rest_framework import serializers
from polls.models import Issue
from .user_serializer import UserSerializer
from rest_framework import filters

class IssueSerializer(serializers.ModelSerializer):
    creador = UserSerializer()
    associat = UserSerializer()
    vigilant = UserSerializer(many=True)
    asignada = UserSerializer()

    filter_backends = [filters.SearchFilter]
    search_fields = ['asunto', 'descripcion']

    class Meta:
        model = Issue
        fields = '__all__'



    