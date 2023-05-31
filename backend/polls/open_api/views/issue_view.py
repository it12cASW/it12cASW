from rest_framework.viewsets import ModelViewSet
from polls.models import Issue, Actividad_Issue, Deadline, Comentario
from polls.consts import status, prioridades, status_order
from django.contrib.auth.models import User
from django.db.models import Q, Max, Case, When, Value, CharField
from django.db import models
from django.http import Http404
from polls.open_api.serializers.issue_serializer import IssueSerializer
from polls.open_api.serializers.user_serializer import UserSerializer
from polls.open_api.serializers.deadline_serializer import DeadlineSerializer
from polls.open_api.serializers.comment_serializer import ComentarioSerializer
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
        if order_field in ['prioridad', 'asunto', 'status', 'modified', 'asignada', 'creador', 'id']:
            if order == 'asc' or not order:
                order = ''
            else:
                order = '-'
            #ordenar las issues
            if order_field == 'prioridad':
                results = issues.annotate(
                    priority_order=Case(
                        When(prioridad='low', then=Value(1)),
                        When(prioridad='normal', then=Value(2)),
                        When(prioridad='high', then=Value(3)),
                        output_field=models.IntegerField(),
                        default=Value(0),
                    )
                ).order_by(order + 'priority_order')
            elif order_field == 'status':
                status_order_case = Case(
                    *[When(status=value, then=Value(position)) for position, value in enumerate(status_order.keys())],
                    output_field=CharField(),
                )
                results = issues.order_by(status_order_case)
                if order == '-':
                    results = results[::-1]
            elif order_field == 'modified':
                max_fecha_actividad = Max('actividades__fecha')
                order_by_field = 'max_fecha_actividad' if order == '' else '-max_fecha_actividad'

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
        creador = Token.objects.get(key=request.auth).user
        asunto = request.data['asunto']
        descripcion = request.data['descripcion']
        # Creo la issue
        issue = Issue(asunto=asunto, descripcion=descripcion, creador=creador)

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
        if blocked != None:
            issue.blocked = blocked

        # REASON_BLOQUED
        reason_blocked = request.data['reason_blocked']
        if reason_blocked:
            issue.reason_blocked = reason_blocked

        # DEADLINE
        dline = False
        deadline = request.data['deadline']
        if deadline:
            dline = True
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
        if dline: 
            deadlineObj = Deadline(issue=issue, deadline=deadline, motivo='')
            deadlineObj.save()

        issue.save()

        # Añado una actividad
        actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,  creador=issue.creador, tipo='Creación', fecha=datetime.now())
        actividad.save()


        return Response({'message': 'Issue creado correctamente', 'issue': IssueSerializer(issue).data}, status=status.HTTP_201_CREATED)

    @action(methods=['put'], detail=True, url_path='edit')
    def editIssue(self, request, pk=None):

        # Compruebo que estan todos los campos y que la issue existe
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)

        editor = Token.objects.get(key=request.auth).user

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
        dline = False
        deadline = request.data['deadline']
        if deadline:
            dline = True
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

        if dline: 
            deadlineObj = Deadline(issue=issue, deadline=deadline, motivo='')
            deadlineObj.save()
        # El editor del issue es el usuario al que pertenece el token

        actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.now(), tipo="editar", usuario=editor)
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
 
    @action(methods=['get','put'], detail=True, url_path='associated')
    def Associated(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1: 
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':

            if issue.associat: 
                return Response({'message': 'La issue ya tiene un usuario associado'}, status=status.HTTP_409_CONFLICT)
        
            idUser = request.data['idUser'] 
            #si el usuario no existe mensage de error
            if not User.objects.filter(id=idUser).exists():
                return Response({'message': 'El asociado no existe'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.get(id=idUser)
            issue.associat = user
            issue.save()

            actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                        creador=issue.creador, tipo='Add Associated', fecha=datetime.now())
            actividad.save()

            return Response({'message': 'Se ha asociado correctamente el usuario a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)
        elif request.method == 'GET':
            if not issue.associat:
                return Response({'message': 'La issue no tiene un usuario asociado'}, status=status.HTTP_400_BAD_REQUEST)
            user = issue.associat
            return Response({'associated': UserSerializer(user).data}, status=status.HTTP_200_OK)
        
        
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

        actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Delete Associated', fecha=datetime.now())
        actividad.save()

        issue.save()

        return Response({'message': 'Se ha eliminado correctamente el usuario asociado a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)

    @action(methods=['get','put'], detail=True, url_path='asigned')
    def Asigned(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1: 
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            if issue.asignada: 
                return Response({'message': 'La issue ya tiene un usuario asignado'}, status=status.HTTP_409_CONFLICT)
            idUser = request.data['idUser'] 
            #si el usuario no existe mensage de error
            if not User.objects.filter(id=idUser).exists():
                return Response({'message': 'El usuario a asignar no existe'}, status=status.HTTP_400_BAD_REQUEST)
        
            user = User.objects.get(id=idUser)
            issue.asignada = user
            issue.save()

            actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                        creador=issue.creador, tipo='Add Assigned', fecha=datetime.now())
            actividad.save()

            return Response({'message': 'Se ha asignado correctamente el usuario a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)
        elif request.method == 'GET':
            if not issue.asignada:
                return Response({'message': 'La issue no tiene un usuario asignado'}, status=status.HTTP_400_BAD_REQUEST)
            user = issue.asignada

            return Response({'asignada': UserSerializer(user).data}, status=status.HTTP_200_OK)
        
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

        actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Delete Assigned', fecha=datetime.now())
        actividad.save()

        return Response({'message': 'Se ha eliminado correctamente el usuario asignado a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)

    @action(methods=['get','put'], detail=True, url_path='watchers')
    def Watchers(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            users = issue.vigilant.all()
            return Response({'message': 'Se ha obtenido a los vigilantes correctamente','vigilant': UserSerializer(users, many=True).data}, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            idUser = request.data['idUser']
            if not User.objects.filter(id=idUser).exists():
                return Response({'message': 'El usuario vigilante no existe'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(id=idUser)
            if issue.vigilant.filter(id=user.id).exists():
                return Response({'message': 'El usuario ya es vigilante de la issue'}, status=status.HTTP_409_CONFLICT)
            issue.addWatcher(user)

            actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                        creador=issue.creador, tipo='Add Watcher', fecha=datetime.now())
            actividad.save()

            return Response({'message': 'Se ha añadido al vigilante correctamente a la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)
        
    @action(methods=['put'], detail=True, url_path='watchers/delete')
    def deleteWatchers(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        idUser = request.data['idUser']
        if not User.objects.filter(id=idUser).exists():
            return Response({'message': 'El usuario vigilante no existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not User.objects.filter(id=idUser).exists():
            return Response({'message': 'El usuario a asignar no existe'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(id=idUser)
        #verificams que el usuario sea vigilante
        if not issue.vigilant.filter(id=user.id).exists():
            return Response({'message': 'El usuario no es vigilante de la issue'}, status=status.HTTP_400_BAD_REQUEST)
        #se borra el vigilante de la issue
        issue.vigilant.remove(user)
        issue.save()

        actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Delete Watcher', fecha=datetime.now())
        actividad.save()
        return Response({'message': 'Se ha eliminado al vigilante correctamente de la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=True, url_path='watchers/deleteAll')
    def deleteAllWatchers(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        #si la issue no tiene vigilantes
        if not issue.vigilant.all():
            return Response({'message': 'La issue no tiene vigilantes que eliminar'}, status=status.HTTP_400_BAD_REQUEST)
        #se borran todos los vigilantes de la issue
        issue.vigilant.clear()
        issue.save()

        actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Delete All Watchers', fecha=datetime.now())
        actividad.save()

        return Response({'message': 'Se han eliminado todos los vigilantes correctamente de la issue', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='bulk-insert')
    def bulkInsert(self, request, pk=None):
        asuntos = request.data['asuntos'] if 'asuntos' in request.data else []
        
        for asunto in asuntos:
            issue = Issue(asunto=asunto, creador=Token.objects.get(key=request.auth).user)
            issue.save()

            actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                        creador=issue.creador, tipo='Creación', fecha=datetime.now())
            actividad.save()
        return Response({'message': 'Issues creades correctamente'} ,status=status.HTTP_201_CREATED)

    
    @action(methods=['get', 'post'], detail=True, url_path='deadline')
    def Deadline(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            if not issue.deadline:
                return Response({'message': 'La issue no tiene deadline'}, status=status.HTTP_400_BAD_REQUEST)
            if not Deadline.objects.filter(issue=issue).exists():
                return Response({'message': 'La issue no tiene deadline'}, status=status.HTTP_400_BAD_REQUEST)
            deadline = Deadline.objects.get(issue=issue)
            return Response({'message': 'Se ha obtenido la deadline de la issue correctamente', 'deadline': DeadlineSerializer(deadline).data}, status=status.HTTP_200_OK)
        if request.method == 'POST':
            if issue.deadline:
                return Response({'message': 'La issue ya tiene deadline'}, status=status.HTTP_409_CONFLICT)
            deadline = request.data['deadline']
            if not deadline:
                return Response({'message': 'Introduce la fecha limite'}, status=status.HTTP_400_BAD_REQUEST)
            motivo = request.data['motivo']
            issue.setDeadline(deadline, motivo)
            deadlineObj = Deadline.objects.get(issue=issue)

            actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                        creador=issue.creador, tipo='Deadline Added', fecha=datetime.now())
            actividad.save()

            return Response({'message': 'Se ha añadido la deadline a la issue correctamente', 'issue': IssueSerializer(issue).data, 'deadline': DeadlineSerializer(deadlineObj).data}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True, url_path='deadline/delete')
    def deleteDeadline(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if not issue.deadline:
            return Response({'message': 'La issue no tiene deadline'}, status=status.HTTP_400_BAD_REQUEST)
        if not Deadline.objects.filter(issue=issue).exists():
            return Response({'message': 'La issue no tiene deadline'}, status=status.HTTP_400_BAD_REQUEST)
        deadline = Deadline.objects.get(issue=issue)
        issue.deadline = None
        issue.save()
        deadline.delete()

        actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Deadline Removed', fecha=datetime.now())
        actividad.save()

        return Response({'message': 'Se ha eliminado la deadline de la issue correctamente', 'issue': IssueSerializer(issue).data}, status=status.HTTP_200_OK)            

    @action(methods=['get', 'post'], detail=True, url_path='comments')
    def Comments(self, request, pk=None):
        try:
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
            
        if issue.deleted == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            comments = Comentario.objects.filter(issue=issue)
            comment_serializer = ComentarioSerializer(comments, many=True)  # Serializar una lista de comentarios
            return Response({'message': 'Se han obtenido los comentarios de la issue correctamente', 'comments': comment_serializer.data}, status=status.HTTP_200_OK)
        if request.method == 'POST':
            comment = request.data['comment']
            if not comment:
                return Response({'message': 'Introduce el comentario'}, status=status.HTTP_400_BAD_REQUEST)
            comentario = Comentario(issue=issue, autor=Token.objects.get(key=request.auth).user, contenido=comment, fecha=datetime.now(), deleted=False)
            comentario.save()
            
            actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Nuevo Comentario', fecha=datetime.now())
            actividad.save()
            
            comment_serializer = ComentarioSerializer(comentario)  # Serializar un solo comentario
            return Response({'message': 'Se ha añadido el comentario a la issue correctamente', 'comment': comment_serializer.data}, status=status.HTTP_201_CREATED)

    
    @action(methods=['post'], detail=True, url_path='comments/delete')
    def deleteComments(self, request, pk=None):
        try: 
            issue = self.get_object()
        except Http404:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        if issue.delete == 1:
            return Response({'message': 'La issue no existe'}, status=status.HTTP_404_NOT_FOUND)
        idComment = request.data['idComment']
        if not idComment:
            #borrar todos los comentarios
            comments = Comentario.objects.filter(issue=issue)
            for comment in comments:
                comment.delete()
            actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Todos los comentarios Borrados', fecha=datetime.now())
            actividad.save()
            return Response({'message': 'Se han eliminado todos los comentarios de la issue correctamente' }, status=status.HTTP_200_OK)
        if not Comentario.objects.filter(id=idComment).exists():
            return Response({'message': 'El comentario no existe'}, status=status.HTTP_400_BAD_REQUEST)
        comment = Comentario.objects.get(id=idComment)
        comment.delete()
        actividad = Actividad_Issue(issue=issue, usuario=Token.objects.get(key=request.auth).user,
                                    creador=issue.creador, tipo='Comentario Borrado', fecha=datetime.now())
        actividad.save()
        #enviar la issue, con los comentarios actuales
        comments = Comentario.objects.filter(issue=issue)
        return Response({'message': 'Se ha eliminado el comentario de la issue correctamente', 'comments': ComentarioSerializer(comments, many=True).data}, status=status.HTTP_200_OK)
        