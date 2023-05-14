from rest_framework.viewsets import ModelViewSet
from polls.models import Issue, Actividad_Issue
from polls.consts import status, prioridades, status_order
from django.contrib.auth.models import User
from django.db.models import Q, Max, Case, When, Value, CharField
from django.db import models
from django.http import Http404
from polls.open_api.serializers.issue_serializer import IssueSerializer
from rest_framework.decorators import api_view, action
from rest_framework import request
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
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
        search = self.request.query_params.get('search')
        status_f = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        creator = self.request.query_params.get('creator')
        assigned = self.request.query_params.get('assigned')
        asociated = self.request.query_params.get('asociated')

        order_field = self.request.query_params.get('order_field')
        order = self.request.query_params.get('order')
        
        filters = Q(deleted=False)
        #busqueda de issues por los campos
        if search:
            filters &= (Q(asunto__icontains=search) | Q(descripcion__icontains=search))
        #para filtrar por los campos
        if status_f:
            filters &= Q(status=status_f)
        if priority:
            filters &= Q(prioridad=priority)
        if creator:
            filters &= Q(creador__username__icontains=creator)
        if assigned:
            filters &= Q(asignada__username__icontains=assigned)
        if asociated:
            filters &= Q(associat__username__icontains=asociated)
        #obtenemos los datos filtrados
        issues = Issue.objects.filter(filters)
        if order_field in ['prioridad', 'asunto', 'status', 'modified', 'asignada', 'creador']:
            if order == 'asc' or not order:
                order = ''
            else:
                order = '-'
            #ordenar las issues
            if order_field == 'prioridad':
                results = issues.annotate(
                    priority_order=Case(
                        When(prioridad='baja', then=Value(1)),
                        When(prioridad='media', then=Value(2)),
                        When(prioridad='alta', then=Value(3)),
                        output_field=models.IntegerField(),
                        default=Value(0),
                    )
                ).order_by('priority_order' if order == 'asc' else '-priority_order')
            elif order_field == 'status':
                status_order_case = Case(
                    *[When(status=value, then=Value(position)) for position, value in enumerate(status_order.keys())],
                    output_field=CharField(),
                )
                results = issues.order_by(status_order_case)
                if order == 'desc':
                    results = results[::-1]
            elif order_field == 'modified':
                max_fecha_actividad = Max('actividades__fecha')
                order_by_field = 'max_fecha_actividad' if order == 'desc' else '-max_fecha_actividad'

                results = issues.annotate(
                    max_fecha_actividad=max_fecha_actividad
                ).order_by(order_by_field)
            elif order_field == 'asignada':
                results = issues.order_by(order + 'asignada__username')
            elif order_field == 'creador':
                results = issues.order_by(order + 'creador__username')
            else:
                results = issues.order_by(order + order_field)
            return results
        #en caso de que no se especifique el orden se ordena por prioridad enviamos las issues
        else: 
            return issues


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
    
    @action(methods=['put'], detail=True, url_path='associated')
    def addAssociated(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1: 
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        elif issue.associat: 
            return Response({'message': 'La issue ya tiene un usuario associado'}, status=status.HTTP_409_CONFLICT)
        idUser = request.data['idUser'] 
        #si el usuario no existe mensage de error
        if not User.objects.filter(id=idUser).exists():
            return Response({'message': 'El asociado no existe'}, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.get(id=idUser)
        issue.associat = user
        issue.save()

        return Response({'message': 'Se ha asociado correctamente el usuario a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)
    
    @action(methods=['delete'], detail=True, url_path='associated/delete')
    def deleteAssociated(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1: 
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        elif not issue.associat: 
            return Response({'message': 'La issue no tiene un usuario asociado'}, status=status.HTTP_400_BAD_REQUEST)
        
        issue.associat = None
        issue.save()

        return Response({'message': 'Se ha eliminado correctamente el usuario asociado a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, url_path='asigned')
    def addAsigned(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1: 
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        elif issue.asignada: 
            return Response({'message': 'La issue ya tiene un usuario asignado'}, status=status.HTTP_409_CONFLICT)
        idUser = request.data['idUser'] 
        #si el usuario no existe mensage de error
        if not User.objects.filter(id=idUser).exists():
            return Response({'message': 'El usuario a asignar no existe'}, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.get(id=idUser)
        issue.asignada = user
        issue.save()

        return Response({'message': 'Se ha asignado correctamente el usuario a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)
    
    @action(methods=['delete'], detail=True, url_path='asigned/delete')
    def deleteAsigned(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1: 
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        elif not issue.asignada: 
            return Response({'message': 'La issue no tiene un usuario asignado'}, status=status.HTTP_400_BAD_REQUEST)
        
        issue.asignada = None
        issue.save()

        return Response({'message': 'Se ha eliminado correctamente el usuario asignado a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)
            