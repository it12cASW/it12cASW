from django.shortcuts import render
from polls.models import Issue, Actividad_Issue, Equipo
from django.contrib.auth.models import User
import datetime




def pantallaCrearEquipo(request):

    return render(request, 'crearEquipo.html')

def crearEquipo(request):


    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        descripcion = request.GET.get('descripcion')
        creador = User.objects.get(id=request.user.id)
        equipo = Equipo(nombre=nombre, descripcion=descripcion, creador=creador)
        equipo.save()

        equipos = Equipo.objects.all()
        issues = Issue.objects.filter(creador_id=request.user.id, deleted=False)
        
    return render(request, 'main.html', {'issues' : issues, 'equipos' : equipos})
