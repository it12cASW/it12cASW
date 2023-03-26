from django.http import HttpResponse
from .models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def register(request):
    # quiero obtener todos los datos que me llegan de la request que sera de tipo POST
    aux = request.GET
    if aux:
        # quiero obtener todos los parametros para crear un nuevo User
        nombre = aux.get('nombre')
        apellidos = aux.get('apellidos')
        email = aux.get('email')
        password = aux.get('password')
        confirmarPassword = aux.get('confirmarPassword')
        user = User(email=email)

        # Compruebo que las contraseñas coinciden
        if (password != confirmarPassword):
            return HttpResponse("Las contraseñas no coinciden", status=400)
        # Compruebo que el usuario no existe
        if user.existeEnDB():
            return HttpResponse("El usuario ya existe", status=400)

        # Creo el usuario
        user.setAtributos(nombre, apellidos, email, password)
        user.guardarEnBD()
        return HttpResponse("SE HA GUARDADO EL USUARIO!!!!", status=200)
    else:
        # devuelve un codigo 400
        return HttpResponse("No hay datos", status=400)


def login(request):

    aux = request.GET
    if aux:

        email = aux.get('email')
        password = aux.get('password')
        # haz una llamada a la funcion estatica de la clase user 'getUsuarioConEmail'
        if User.getUsuarioConEmail(email):
            return HttpResponse("El usuario existe", status=200)
        else:
            return HttpResponse("El usuario no existe", status=400)

    return HttpResponse("Faltan parámetros ", status="400")
