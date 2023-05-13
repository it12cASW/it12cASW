from rest_framework.viewsets import ModelViewSet
from polls.models import Issue
from django.contrib.auth.models import User
from polls.open_api.serializers.issue_serializer import IssueSerializer
from rest_framework.decorators import api_view, action
from rest_framework import request
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes

from rest_framework import status
from rest_framework.response import Response



class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    @action(methods=['get'], detail=False, url_path='issues')
    def get_queryset(self):

        # Comprobamos el token
        param = authorization_header = self.request.META['HTTP_AUTHORIZATION']
        token = authorization_header.split()[1]
        token_object = Token.objects.filter(key=token).first()
        
        # Check if token is valid
        if not token_object:
            return Response({'message': 'Token is not valid'}, status=status.HTTP_401_UNAUTHORIZED)

        # Buscar los issues con 'deleted' a 0
        result = Issue.objects.filter(deleted=0)
        return result

    # http://127.0.0.1:8000/api/issues/create/
    
    # {
    #     "data": {
    #         "id_creador": 1,
    #         "asunto": "ASUNTO TEST API 1",
    #         "descripcion": "ASUNTO TEST API 1",
    #         "asignado": 1,
    #         "asociado": 2,
    #         "blocked": true,
    #         "reason_blocked": "bloqueado para test",
    #         "deadline": "2023-04-21 00:00:00",
    #         "prioridad": "baja",
    #         "status": "cancelado"
    #     }   
    # }

    @action(methods=['post'], detail=False, url_path='create')
    def createIssue(self, request, format=None):
        
        # Comprobamos el token
        param = authorization_header = self.request.META['HTTP_AUTHORIZATION']
        token = authorization_header.split()[1]
        token_object = Token.objects.filter(key=token).first()

        # Check if token is valid
        if not token_object:
            return Response({'message': 'Token is not valid'}, status=status.HTTP_401_UNAUTHORIZED)

        # Compruebo que estan todos los campos
        id_creador = request.data['data']['id_creador']
        asunto = request.data['data']['asunto']
        descripcion = request.data['data']['descripcion']

        if not id_creador or not asunto or not descripcion:
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Creo la issue
        creadorObj = User.objects.get(id=id_creador)
        issue = Issue(asunto=asunto, descripcion=descripcion, creador=creadorObj)

        # ASOCIADO  
        asociado = request.data['data']['asociado']
        if asociado:
            if not User.objects.filter(id=asociado).exists():
                return Response({'message': 'El asociado no existe'}, status=status.HTTP_409_CONFLICT)
            issue.associat_id = asociado
    
        # ASIGNADO
        asignado = request.data['data']['asignado']
        if asignado:
            if not User.objects.filter(id=asignado).exists():
                return Response({'message': 'El asignado no existe'}, status=status.HTTP_409_CONFLICT)
            issue.asignada_id = asignado

        # BLOCKED
        blocked = request.data['data']['blocked']
        if blocked:
            issue.blocked = blocked

        # REASON_BLOQUED
        reason_blocked = request.data['data']['reason_blocked']
        if reason_blocked:
            issue.reason_blocked = reason_blocked

        # DEADLINE
        deadline = request.data['data']['deadline']
        if deadline:
            issue.deadline = deadline
        
        # PRIORITY
        prioridad = request.data['data']['prioridad']
        if prioridad:
            issue.prioridad = prioridad

        # STATUS
        estado = request.data['data']['status']
        if estado:
            issue.status = estado

        issue.save()
        return Response({'message': 'Issue creado correctamente', 'issue': IssueSerializer(issue).data}, status=status.HTTP_201_CREATED)

    # http://127.0.0.1:8000/api/issues/delete/

    # {
    #     "id_issue": 33
    # }

    @action(methods=['delete'], detail=False, url_path='delete')
    def deleteIssue(self, request, format=None):

        # Comprobamos el token
        param = authorization_header = self.request.META['HTTP_AUTHORIZATION']
        token = authorization_header.split()[1]
        token_object = Token.objects.filter(key=token).first()
        
        # Check if token is valid
        if not token_object:
            return Response({'message': 'Token is not valid'}, status=status.HTTP_401_UNAUTHORIZED)

        # Compruebo que estan todos los campos
        id_issue = request.data['id_issue']
        if not id_issue:
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)

        # Obtengo el usuario que hace al peticion
        # userPeticion = token_object.user
        # userCreador = Issue.objects.get(id=id_issue).creador
        # if userPeticion != userCreador:
        #     return Response({'message': 'Solo el creador puede borrar la issue'}, status=status.HTTP_400_BAD_REQUEST)

        # Borro la issue
        issue = Issue.objects.get(id=id_issue)
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_400_BAD_REQUEST)

        issue.deleted = 1
        issue.save()
        
        return Response({'message': 'Issue borrado correctamente'}, status=status.HTTP_200_OK)

    

    