from rest_framework.viewsets import ModelViewSet
from polls.models import Comentario
from polls.open_api.serializers.comment_serializer import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer