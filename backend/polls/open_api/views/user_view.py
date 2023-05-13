from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from polls.open_api.serializers.user_serializer import UserSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from django.http import request
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False, url_path='users')
    def get_queryset(self):
        result = User.objects.all()
        return result

    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request, format=None):
        data = request.data
        
        if(not data):
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)
        print("usuario y contraseña correctos")
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'User logged in successfully', 'token':token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_404_NOT_FOUND)
    
        

    @action(methods=['post'], detail=False, url_path='register')
    def register(self, request, format=None):
        data = request.data
        if(not data):
            return Response({'message': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)

        username = data['username']
        password = data['password']
        email = data['email']
        
        user = User.objects.filter(username=username).first()
        if(user):
            return Response({'message': 'User already exists'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        serializer = UserSerializer(user)
        return Response({'message': 'User registered successfully', 'token':token.key}, status=status.HTTP_201_CREATED)

    
    
