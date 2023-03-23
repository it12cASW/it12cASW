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
        return HttpResponse("HAY DATOS", status=200)
    else:
        # devuelve un codigo 400
        return HttpResponse("No hay datos", status=400)


def login(request):
    return HttpResponse("Hello, world. You're at the polls login.")
