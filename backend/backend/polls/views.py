from django.http import HttpResponse
from .models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def register(request):
    # quiero obtener todos los datos que me llegan de la request que sera de tipo POST
    aux = request.GET
    # comprueba que aux no esta vacia
    if aux:
        # quiero obtener todos los parametros para crear un nuevo User
        name = aux.get('name')
        email = aux.get('email')
        password = aux.get('password')
        # creo un nuevo usuario
        user = User(name=name, email=email, password=password)

        # devuelve un codigo 200
        return HttpResponse("El usuario se ha guardado correctamente!", status=200)
    else:
        # devuelve un codigo 400
        return HttpResponse("No hay datos", status=400)


def login(request):

    if request.GET:

        # declarame una variable nombre
        email = request.GET.get('name')
        password = request.GET.get('password')

        # comprueba que el usuario existe
        if User.objects.filter(email=email, password=password).exists():
            return HttpResponse("Usuario correcto", status=200)
        else:
            return HttpResponse("Usuario incorrecto", status=400)

    return HttpResponse("Usuario incorrecto", status="400")
