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
from polls.models import Issue, Actividad_Issue, Equipo, Miembro_Equipo

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
            equipos = Equipo.objects.all()
            equipo_usuario = Miembro_Equipo.objects.filter(miembro=user_id)
            return render(request, 'main.html', {"issues" : issues, "equipos" : equipos, "equipo" : equipo_usuario})
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
        

        equipos = Equipo.objects.all()
        return render(request, 'main.html', {"issues" : issues, "equipos" : equipos})
    else:
        return render(request, 'register.html', {"error" : "Algo ha ido mal..."})

# Cerrar sesión de un usuario
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
        equipos = Equipo.objects.all()

        equipo_usuario = Miembro_Equipo.objects.filter(miembro=userBD.id)
        equipo = equipo_usuario[0].equipo

        return render(request, 'main.html', {"issues" : issues, "equipos" : equipos, "equipo" : equipo})

    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    print("miembro_equipo: ", miembro_equipo)
    return render(request, 'main.html', {"issues" : issues, "equipos" : equipos, "equipo" : miembro_equipo})

# Mostrar pantalla de edición de perfil
def editarPerfil(request):

    return render(request, 'editarPerfil.html')

# Guardar los nuevos datos del perfil
def actualizarPerfil(request):

    issues = Issue.objects.filter(creador_id=request.user.id, deleted=False)
    equipos = Equipo.objects.all()

    return render(request, 'main.html', {"issues" : issues, "equipos" : equipos})
    
# Seleccionar equipo
def seleccionarEquipo(request):

    # crea un miembro equipo
    equipo = Equipo.objects.get(id=request.GET['equipo'])
    user = User.objects.get(id=request.user.id)
    miembro_equipo = Miembro_Equipo(equipo=equipo , miembro=user)
    miembro_equipo.save()

    issues = Issue.objects.filter(creador_id=request.user.id, deleted=False)
    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    return render(request, 'main.html', {"issues" : issues, "equipos" : equipos, "equipo" : miembro_equipo})
    
    




