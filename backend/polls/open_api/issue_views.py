from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from polls.serializers.serializers import IssueSerializer
from rest_framework import mixins
from polls.models import Issue


class IssueViews(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

    def get_queryset(self):
        queryset = Issue.objects.all()
        return queryset

    def create(self, request):
        super().create(request)
        return Response({'status': 'Issue created'})

    def update(self, request):
        super(self, request).update(request)
        return Response({'status': 'Issue updated'})
