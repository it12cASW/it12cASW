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
from polls.models import Issue, Actividad_Issue, Equipo, Miembro_Equipo, Imagen_Perfil, Watcher
from django.views.decorators.csrf import csrf_protect

def aux(request):
    return render(request, 'login.html')

# Iniciar sesión de un usuario
@csrf_protect
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
            if equipos != None:
                equipo_usuario = Miembro_Equipo.objects.filter(miembro=user_id)
            return render(request, 'main.html', {"issues" : issues, "equipos" : equipos, "equipo" : equipo_usuario})
        else:

            return render(request, 'login.html', {"error" : "Usuario o contraseña incorrectos"})

    else:
        print("estoy aqui")
        return render(request, 'login.html', {"error" : "Algo ha ido mal..."})

# Registro de un usuario
@csrf_protect
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
        return render(request, 'login.html')
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
        if equipo_usuario:
            equipo = equipo_usuario[0].equipo
        else :
            equipo = None
        return render(request, 'main.html', {"issues" : issues, "equipos" : equipos, "equipo" : equipo})

    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    print("miembro_equipo: ", miembro_equipo)
    return render(request, 'main.html', {"issues" : issues, "equipos" : equipos, "equipo" : miembro_equipo})

# Mostrar pantalla de edición de perfil
def pantallaEditarPerfil(request):

    print("ID: " + str(request.user.id))


    # Obtengo el usuario sobre el que se realizaran las actulaizaciones
    usuario = User.objects.get(id=request.user.id)

    # si existe imagen perfil
    if Imagen_Perfil.objects.filter(usuario=usuario).exists():
        imagenPerfil = Imagen_Perfil.objects.get(usuario=usuario)
    else:
        imagenPerfil = None

    return render(request, 'editarPerfil.html', {"user" : request.user, "imagenPerfil" : imagenPerfil})

# Guardar los nuevos datos del perfil
@csrf_protect
def actualizarPerfil(request):
    
    # Obtengo el usuario sobre el que se realizaran las actulaizaciones
    usuario = User.objects.get(id=request.user.id)
    imagen = request.FILES.get('imagen')
    # crea una instance de imagenPerfil
    if imagen:
        if Imagen_Perfil.objects.filter(usuario=usuario).exists():
            imagenPerfil = Imagen_Perfil.objects.get(usuario=usuario)
            imagenPerfil.imagen = imagen
            imagenPerfil.save()
        else:
            imagenPerfil = Imagen_Perfil(imagen=imagen, usuario=usuario)
            imagenPerfil.save()


    username = request.POST.get('username')
    email = request.POST.get('email')
    nombre = request.POST.get('nombre')
    apellidos = request.POST.get('apellidos')
    about = request.POST.get('about')

    if username != usuario.username:
        if User.objects.filter(username=username).exists():
            return render(request, 'editarPerfil.html', {"user": usuario,"error" : "El usuario ya existe"})
        usuario.username = username
        usuario.save()
    if email != usuario.email:
        if User.objects.filter(email=email).exists():
            return render(request, 'editarPerfil.html', {"user": usuario,"error" : "El email ya existe"})
        usuario.email = email
        usuario.save()
    if nombre != usuario.first_name:
        usuario.first_name = nombre
        usuario.save()
    if apellidos != usuario.last_name:
        usuario.last_name = apellidos
        usuario.save()
    if about != usuario.about:
        usuario.about = about
        usuario.save()

    # si existe imagen perfil
    if Imagen_Perfil.objects.filter(usuario=usuario).exists():
        imagenPerfil = Imagen_Perfil.objects.get(usuario=usuario)
    else:
        imagenPerfil = None


    # Lo guardo y compruebo que todo haya ido bien
    # return render(request, 'editarPerfil.html')
    return render (request, 'editarPerfil.html', {"user": usuario, "imagenPerfil": imagenPerfil, "error" : "Se ha actualizado el perfil correctamente"})
    
    
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
    
# Ver perfil 
def verPerfil(request, username):
    # Obtén el ID de la BD
    user = User.objects.get(username=username)
    about = User.objects.get(about=user.about);

    # obten las actividades de este usuario
    actividades = Actividad_Issue.objects.filter(usuario=user.id)
    # obtengo el equipo del usuario
    if Miembro_Equipo.objects.filter(miembro=user.id):
        equipo_usuario = Miembro_Equipo.objects.filter(miembro=user.id)[0].equipo
    else :
        equipo_usuario = None

    # si existe imagen perfil
    if Imagen_Perfil.objects.filter(usuario=user).exists():
        imagenPerfil = Imagen_Perfil.objects.get(usuario=user)
    else:
        imagenPerfil = None

    watchlist = Watcher.objects.filter(usuario=request.user.id)
    #coger todas las issues de la watchlist
    issues = []
    for i in watchlist:
        issues.append(Issue.objects.get(id=i.issue.id))


    # Obtengo los usuarios para ver sus perfiles
    if User.objects.all().exists():
        usuarios = User.objects.all()
    else:
        usuarios = None

    return render(request, 'verPerfil.html', {"user" : user, "about" : about, "actividades": actividades, "equipo" : equipo_usuario, "imagenPerfil" : imagenPerfil, "issues" : issues, "usuarios": usuarios})





