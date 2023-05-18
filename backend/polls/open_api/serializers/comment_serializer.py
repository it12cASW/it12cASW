from rest_framework.serializers import ModelSerializer
from polls.models import Comentario
from .user_serializer import UserSerializer
from .issue_serializer import IssueSerializer
class ComentarioSerializer(ModelSerializer):
    issue = IssueSerializer()
    autor = UserSerializer()
    class Meta:
        model = Comentario
        fields = '__all__'
