from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from polls.serializers.serializers import IssueSerializer, CommentSerializer, DeadlineSerializer
from rest_framework import mixins
from polls.models import Issue, Comentario, Deadline


class DeadlineView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DeadlineSerializer
    queryset = Deadline.objects.all() # Conjunto de datos que podemos consultar

    def get_queryset(self):
        queryset = Deadline.objects.all()
        return queryset
    
    def create(self, request):
        super().create(request)
        return Response({'status': 'Deadline created'})

    def update(self, request):
        super(self, request).update(request)
        return Response({'status': 'Deadline updated'})
    
    def destroy(self, request):
        super(self, request).destroy(request)
        return Response({'status': 'Deadline deleted'})