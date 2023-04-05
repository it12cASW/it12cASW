from django.http import HttpResponse
from django.shortcuts import render
from social_django.models import UserSocialAuth
#from polls.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

def aux(request):
    return render(request, 'login.html')

# Iniciar sesión de un usuario
def logintest(request):
    if request.method == 'POST':
        # Obtener el nombre de usuario y la contraseña desde la solicitud POST
        username = request.POST['username']
        password = request.POST['password']
        # comprueba si existe
        if User.objects.filter(username=username).exists():
            print("existe")
        else:
            print("no existe")
        # Autenticar al usuario con las credenciales proporcionadas
        print("voy a autenticar")
        user = authenticate(request, username=username, password=password)

        # Si el usuario existe y las credenciales son correctas
        if user is not None:
            print("SE HA LOGEADO EL USUARIO")
            # Iniciar sesión para el usuario
            login(request, user)
            # Redirigir a la página de inicio o cualquier otra página que desees
            return render(request, 'main.html')
        else:
            print("FALLO EN EL LOGIN")
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            return render(request, 'login.html')

    # Si la solicitud no es POST, mostrar la página de inicio de sesión
    else:
        return render(request, 'login.html')

# Registro de un usuario
def register(request):
    # quiero obtener todos los datos que me llegan de la request que sera de tipo POST
    aux = request.POST
    if aux:
        username = aux.get('username')
        email = aux.get('email')
        password = aux.get('password')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html')

        nuevo_usuario = User.objects.create_user(username=username, email=email, password=password)
        nuevo_usuario.save()    
        print("SE HA REGISTRADO EL USUARIO")

        return render(request, 'main.html')
    else:
        return render(request, 'register.html')

#GOOGLE

def login_with_google(request):
    return render(request, 'main.html')




