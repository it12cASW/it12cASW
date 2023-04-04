from django.http import HttpResponse
from django.shortcuts import render
from social_django.models import UserSocialAuth
from polls.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

def aux(request):
    return render(request, 'login.html')

# Iniciar sesión de un usuario
def login(request):
    print("hola")
    aux = request.POST
    if aux:
        email = aux.get('email')
        password = aux.get('password')
        # Crea una usuario
        user = User(email=email)

        if user.existeEnDB():

            print("El usuario existe")
            # Compruebo que la contraseña sea correcta
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                print("Contraseña correcta")
                return render(request, 'main.html')
            else:
                return render(request, 'login.html')
        else:
            print("El usuario no existe")
            return render(request, 'login.html')        

    return render(request, 'login.html')

# Registro de un usuario
def register(request):
    # quiero obtener todos los datos que me llegan de la request que sera de tipo POST
    aux = request.POST
    if aux:
         
        email = aux.get('email')
        password = aux.get('password')
        hashed_password = make_password(password)
        print("EMAIL: " + email + ", PASSWORD: " + password)        
        user = User(email=email, password=hashed_password)

        # Compruebo que el usuario no existe
        if user.existeEnDB():
            print("El usuario existe")
            return render(request, 'register.html')
        else:
            #registro al usuario
            user.guardarEnBD()
            return render(request, 'main.html')
    else:
        return render(request, 'register.html')

#GOOGLE

def login_with_google(request):

    if request.method == 'GET':

        print("Estoy en GET")

        email = request.user.email
        print(user_social.email)
        print("EMAIL: " + email)
        # obtén el token de identificación de Google del usuario
        token = request.GET.get('idtoken')

        # verifica el token con Google
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)

            print("Tengo el id")

            # el token es válido, obtén la información del usuario
            user_id = idinfo['sub']  # identificador único del usuario de Google
            email = idinfo['email']  # dirección de correo electrónico del usuario
            name = idinfo['name']  # nombre del usuario
            picture_url = idinfo['picture']  # URL de la foto de perfil del usuario

            print("EMAIL: " + email + ", NAME: " + name)
            # crea o actualiza el usuario en la base de datos de Django
            user, created = User.objects.get_or_create(email=email)
            user.name = name
            user.picture_url = picture_url
            user.save()

            # inicia sesión en Django
            user = authenticate(request, email=email)
            if user is not None:
                login(request, user)
                return redirect('home')

            console.log("sdfsd")

            # si el usuario no existe, regresa un error
            return render(request, 'login.html', {'error': 'No se pudo iniciar sesión con Google.'})
        except ValueError:
            # el token es inválido
            return render(request, 'login.html', {'error': 'No se pudo iniciar sesión con Google.'})
    else:
        print("NO ES GET")
        # renderiza la página de inicio de sesión con Google
        return render(request, 'login.html')




