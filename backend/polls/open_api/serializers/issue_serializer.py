from rest_framework import serializers
from polls.models import Issue
from .user_serializer import UserSerializer

class IssueSerializer(serializers.ModelSerializer):
    creador = UserSerializer()
    associat = UserSerializer()
    vigilant = UserSerializer(many=True)
    asignada = UserSerializer()

    class Meta:
        model = Issue
        fields = '__all__'



    