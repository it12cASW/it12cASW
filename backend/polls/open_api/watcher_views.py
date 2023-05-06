from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from polls.serializers.serializers import WatcherSerializer
from rest_framework import mixins
from polls.models import Watcher


class WatcherViews(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = WatcherSerializer
    queryset = Watcher.objects.all() # Conjunto de datos que podemos consultar

    def get_queryset(self):
        queryset = Watcher.objects.all()
        return queryset

    def create(self, request):
        super().create(request)
        return Response({'status': 'Watcher created'})

    def update(self, request):
        super(self, request).update(request)
        return Response({'status': 'Watcher updated'})