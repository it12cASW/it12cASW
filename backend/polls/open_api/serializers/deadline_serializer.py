from rest_framework import serializers
from polls.models import Deadline

class DeadlineSerializer(serializers.ModelSerializer):
    issue_id = serializers.IntegerField(source='issue.id')

    class Meta:
        model = Deadline
        fields = ['issue_id', 'deadline', 'motivo']
