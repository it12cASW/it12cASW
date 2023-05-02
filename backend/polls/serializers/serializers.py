from rest_framework import serializers
from polls.models import Issue
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.asunto)
        instance.email = validated_data.get('email', instance.descripcion)
        instance.password = validated_data.get('password', instance.creador)
        instance.save()
        return instance

class IssueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    asunto = serializers.CharField(max_length=50)
    descripcion = serializers.CharField(max_length=200)
    creador = UserSerializer(required=False)
    associat = UserSerializer(required=False)
    vigilant = UserSerializer(many=True)
    deleted = serializers.BooleanField(default=False)
    asignada = UserSerializer()
    blocked = serializers.BooleanField(default=False, required=False)
    reason_blocked = serializers.CharField(max_length=200, required=False)
    deadline = serializers.DateTimeField(required=False)
    prioridad = serializers.CharField(max_length=100, required=False)
    status = serializers.CharField(max_length=100, required=False)


    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.asunto = validated_data.get('asunto', instance.asunto)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.creador = validated_data.get('creador', instance.creador)
        instance.associat = validated_data.get('associat', instance.associat)
        instance.vigilant = validated_data.get('vigilant', instance.vigilant)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.asignada = validated_data.get('asignada', instance.asignada)
        instance.blocked = validated_data.get('blocked', instance.blocked)
        instance.reason_blocked = validated_data.get('reason_blocked', instance.reason_blocked)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.prioridad = validated_data.get('prioridad', instance.prioridad)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

