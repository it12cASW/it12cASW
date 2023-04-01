from django.http import HttpResponse
from django.shortcuts import render

from backend.polls.models import User, Issue
from django.core import serializers

class IssueViewset(object):
    def get(self, request):
        issues = Issue.objects.all()
        return render(request, 'issues.html', {'issues': issues})


