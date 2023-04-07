from django.http import HttpResponse
from django.shortcuts import render
from social_django.models import UserSocialAuth
#from polls.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import logout
from polls.views import issue_viewset
from polls.models import Issue

def aux(request):
    return render(request, 'login.html')

# Iniciar sesión de un usuario
def logintest(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists(): print("existe")
        else: print("no existe")

        print("voy a autenticar")
        user = authenticate(request, username=username, password=password)
        print("autenticado")
        if user is not None:
            print("estoy aqui")
            login(request, user)
            print("estoy aqui323")
            # OBTEN EL ID DE LA BD
            user_id = User.objects.get(username=username).id
            print("tengo el id")
            issues = Issue.objects.filter(creador_id=user_id, deleted=False)
            if issues:
                print("existen")
                return render(request, 'main.html', {"issues" : issues})
            return render(request, 'main.html')
        else:

            return render(request, 'login.html', {"error" : "Usuario o contraseña incorrectos"})

    else:
        print("estoy aqui")
        return render(request, 'login.html', {"error" : "Algo ha ido mal..."})

# Registro de un usuario
def register(request):
    # quiero obtener todos los datos que me llegan de la request que sera de tipo POST
    aux = request.POST
    if aux:
        username = aux.get('username')
        email = aux.get('email')
        password = aux.get('password')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {"error" : "El usuario ya existe"})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {"error" : "El email ya existe"})

        nuevo_usuario = User.objects.create_user(username=username, email=email, password=password)
        nuevo_usuario.save()    
        print("SE HA REGISTRADO EL USUARIO")
        
        return render(request, 'main.html')
    else:
        return render(request, 'register.html', {"error" : "Algo ha ido mal..."})

def logoutTest(request):
    logout(request)
    return render(request, 'login.html')

#GOOGLE
def login_with_google(request):

    # Obtén el ID de la BD
    user = request.user
    user = str(user)
    # obten el user identificado con usermane = user
    userBD = User.objects.get(username=user)
    
    if User.objects.filter(id=userBD.id).exists():
        issues = Issue.objects.filter(creador_id=userBD.id,  deleted=False)
        return render(request, 'main.html', {"issues" : issues})

    return render(request, 'main.html', {"issues" : issues})

def editarPerfil(request):

    return render(request, 'editarPerfil.html')


def actualizarPerfil(request):

    return render(request, 'main.html')
    




