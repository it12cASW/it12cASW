from rest_framework.viewsets import ModelViewSet
from polls.models import Comentario
from polls.open_api.serializers.comment_serializer import ComentarioSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    
    def get_queryset(self):

        queryset = self.queryset
        queryset = queryset.filter(deleted=False)
        if self.request.query_params.get('issue_id') is not None:
            queryset = queryset.filter(issue=self.request.query_params.get('issue_id'))
        else:
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        if(not data):
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)
        issue_id = data['issue_id']
        text = data['text']

        comentario = Comentario.objects.create(issue_id=issue_id, autor=Token.objects.get(key=request.auth).user, contenido=text)
        comentario.save()
        return Response({'message': 'Comentario creado correctamente'}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        comentario = self.queryset.get(id=self.kwargs['pk'])
        if(comentario.autor != Token.objects.get(key=request.auth).user):
            return Response({'message': 'No tienes permiso para borrar este comentario'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            if comentario.deleted:
                return Response({'message': 'El comentario ya está borrado'}, status=status.HTTP_400_BAD_REQUEST)
            comentario.deleted = True
            comentario.save()
            return Response({'message': 'Comentario borrado correctamente'}, status=status.HTTP_200_OK)