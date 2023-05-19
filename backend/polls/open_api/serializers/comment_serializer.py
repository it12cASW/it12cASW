from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from polls.models import Comentario
from .user_serializer import UserSerializer
from .issue_serializer import IssueSerializer

class ComentarioSerializer(ModelSerializer):
    issue_id = serializers.IntegerField(source='issue.id')
    autor = UserSerializer()
    class Meta:
        model = Comentario
        fields = ['id', 'issue_id', 'autor', 'contenido', 'fecha']
