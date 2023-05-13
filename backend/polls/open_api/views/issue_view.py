from rest_framework.viewsets import ModelViewSet
from polls.models import Issue, Actividad_Issue
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
from datetime import datetime

class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    @action(methods=['get'], detail=False, url_path='issues')
    def get_queryset(self):

        result = Issue.objects.filter(deleted=False)
        return result

    @action(methods=['post'], detail=False, url_path='create')
    def createIssue(self, request, format=None):
        # Compruebo que estan todos los campos
        id_creador = request.data['id_creador']
        asunto = request.data['asunto']
        descripcion = request.data['descripcion']

        if not id_creador or not asunto or not descripcion:
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Creo la issue
        creadorObj = User.objects.get(id=id_creador)
        issue = Issue(asunto=asunto, descripcion=descripcion, creador=creadorObj)

        # ASOCIADO  
        asociado = request.data['asociado']
        if asociado:
            if not User.objects.filter(id=asociado).exists():
                return Response({'message': 'El asociado no existe'}, status=status.HTTP_409_CONFLICT)
            issue.associat_id = asociado
    
        # ASIGNADO
        asignado = request.data['asignado']
        if asignado:
            if not User.objects.filter(id=asignado).exists():
                return Response({'message': 'El asignado no existe'}, status=status.HTTP_409_CONFLICT)
            issue.asignada_id = asignado

        # BLOCKED
        blocked = request.data['blocked']
        if blocked:
            issue.blocked = blocked

        # REASON_BLOQUED
        reason_blocked = request.data['reason_blocked']
        if reason_blocked:
            issue.reason_blocked = reason_blocked

        # DEADLINE
        deadline = request.data['deadline']
        if deadline:
            issue.deadline = deadline
        
        # PRIORITY
        prioridad = request.data['prioridad']
        if prioridad:
            issue.prioridad = prioridad

        # STATUS
        estado = request.data['status']
        if estado:
            issue.status = estado

        issue.save()

        # Añado una actividad

        return Response({'message': 'Issue creado correctamente', 'issue': IssueSerializer(issue).data}, status=status.HTTP_201_CREATED)

    # http://127.0.0.1:8000/api/issues/delete/

    # {
    #     "id_issue": 33
    # }

    @action(methods=['delete'], detail=False, url_path='delete')
    def deleteIssue(self, request, format=None):        
        # Compruebo que estan todos los campos
        id_issue = request.data['id_issue']
        if not id_issue:
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)
        elif not Issue.objects.filter(id=id_issue).exists():
            return Response({'message': 'La issue no existe'}, status=status.HTTP_400_BAD_REQUEST)

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

    @action(methods=['put'], detail=False, url_path='edit')
    def editIssue(self, request, format=None):
        # Compruebo que estan todos los campos y que la issue existe
        id_issue = request.data['id_issue']
        if not id_issue:
            return Response({'message': 'Introduce la id de la issue'}, status=status.HTTP_400_BAD_REQUEST)
        elif not Issue.objects.filter(id=id_issue).exists() or Issue.objects.get(id=id_issue).deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        editor_id = request.data['id_user']
        if not editor_id:
            return Response({'message': 'Introduce el id del usuario que edita'}, status=status.HTTP_400_BAD_REQUEST)
        elif not User.objects.filter(id=editor_id).exists():
            return Response({'message': 'El usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        issue = Issue.objects.get(id=id_issue)

        # Asunto
        asunto = request.data['asunto']
        if asunto:
            issue.asunto = asunto

        # Descripcion
        descripcion = request.data['descripcion']
        if descripcion:
            issue.descripcion = descripcion

        # Prioridad
        asignado = request.data['asignado']
        if asignado:
            if not User.objects.filter(id=asignado).exists():
                return Response({'message': 'El asignado no existe'}, status=status.HTTP_409_CONFLICT)
            issue.asignada_id = asignado

        # Asociado
        asociado = request.data['asociado']
        if asociado:
            if not User.objects.filter(id=asociado).exists():
                return Response({'message': 'El asociado no existe'}, status=status.HTTP_409_CONFLICT)
            issue.associat_id = asociado

        # Bloqueado
        blocked = request.data['blocked']
        if blocked:
            issue.blocked = blocked

        # Reason_blocked
        reason_blocked = request.data['reason_blocked']
        if reason_blocked:
            issue.reason_blocked = reason_blocked

        # Deadline
        deadline = request.data['deadline']
        if deadline:
            issue.deadline = deadline

        # Prioridad
        prioridad = request.data['prioridad']
        if prioridad:
            issue.prioridad = prioridad

        # Estado
        estado = request.data['status']
        if estado:
            issue.status = estado

        issue.save()

        # Añado una actividad fecha, tipo, creador_ir, issue_id, usuario_id
        editorObj = User.objects.get(id=editor_id)
        actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.now(), tipo="editar", usuario=editorObj)
        actividad.save()

        return Response({'message': 'Issue editada correctamente', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='delete')
    def deleteIssue(self, request, pk=None):
        # Compruebo que estan todos los campos
        issue = self.get_object()
        if not issue:
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)

        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_400_BAD_REQUEST)

        issue.deleted = 1
        issue.save()
        
        return Response({'message': 'Issue borrado correctamente'}, status=status.HTTP_200_OK)
    
    @action(methods=['put'], detail=True, url_path='addAsociated')
    def addAsociated(self, request, pk=None):
        issue = self.get_object()
        if not issue or issue.deleted == 1: 
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        elif issue.associat: 
            return Response({'message': 'La issue ya tiene un usuario associado'}, status=status.HTTP_400_BAD_REQUEST)
        idUser = request.data['idUser'] 
        #si el usuario no existe mensage de error
        if not User.objects.filter(id=idUser).exists():
            return Response({'message': 'El asociado no existe'}, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.get(id=idUser)
        issue.associat = user
        issue.save()

        return Response({'message': 'Se ha asociado correctamente el usuario a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)
        

        
            