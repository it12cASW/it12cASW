from django.shortcuts import render
from polls.models import Issue, Actividad_Issue, Equipo, Miembro_Equipo
from django.contrib.auth.models import User
import datetime




# Mostrar pantalla de creación de un issue
def pantallaCrearIssue(request):
    usuario = User.objects.get(id=request.user.id)

    if Miembro_Equipo.objects.filter(miembro=usuario):
        equipo = Miembro_Equipo.objects.filter(miembro=request.user)
        miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
        usuarios = []
        for miembro in miebros:
            usuarios.append(miembro.miembro)

        sinAsignar = User(username="sin asignar")
        usuarios.append(sinAsignar)
        return render(request, 'crearIssue.html', {'usuarios' : usuarios})
    else:
        return render(request, 'crearIssue.html')

# Crear un nuevo issue
def crearIssue(request):

    # Obtengo los miembros
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    usuarios = []
    if equipo:
        miembros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
        for miembro in miembros:
            usuarios.append(miembro.miembro)
        sinAsignar = User(username="sin asignar")
        usuarios.append(sinAsignar)

    if request.method == 'GET':
        if request.GET.get('asunto') != '':
            asunto = request.GET.get('asunto')
            descripcion = request.GET.get('descripcion')
            creador = User.objects.get(id=request.user.id)
            asignado = request.GET.get('type')

            if asignado == "sin asignar":
                asignado = None
            else:
                if: User.objects.get(username=asignado)
                    usuario_asignado = User.objects.get(username=asignado)
                else:
                    asignado = None

            issue = Issue(asunto=asunto, descripcion=descripcion, creador=creador, asignada=usuario_asignado)
            issue.save()
        
            actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="creada", usuario=request.user)
            actividad.save()
        
        else:
            return render(request, 'crearIssue.html', {'error' : 'El asunto no puede estar vacío', 'usuarios' : usuarios})
        
    return render(request, 'crearIssue.html', {'error' : "Se ha creado el issue correctamente", 'usuarios' : usuarios})

# Mostrar la información del issue dado su id
def mostrarIssue(request, idIssue):
    # obten el issue con este id
    issue = Issue.objects.get(id=idIssue)
    creador = User.objects.get(id=issue.creador.id)
    actividades = Actividad_Issue.objects.filter(issue_id=idIssue)
    return render(request, 'mostrarIssue.html', {'issue': issue, 'creador' : creador, 'actividades' : actividades })

# Eliminar un issue dado su id
def eliminarIssue(request, idIssue):

    issue = Issue.objects.get(id=idIssue)
    # modifica el atributo 'deleted' a True
    issue.deleted = True
    issue.save()
    return render(request, 'eliminarIssue.html', { 'issue': issue })

# Mostrar pantalla de edición de un issue
def mostrarPantallaEditarIssue(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    creador = User.objects.get(id=issue.creador.id)

    

    if Miembro_Equipo.objects.filter(miembro=creador):
        equipo = Miembro_Equipo.objects.filter(miembro=creador)[0].equipo
        miembros = Miembro_Equipo.objects.filter(equipo=equipo)
        aux = []
        for miembro in miembros:
            aux.append(miembro.miembro)
        sinAsignar = User(username="sin asignar")
        aux.append(sinAsignar)
        return render(request, 'editarIssue.html', {'issue': issue, 'creador' : creador, 'usuarios' : aux })

    return render(request, 'editarIssue.html', {'issue': issue, 'creador' : creador})

# Acualizar el issue con la nueva información
def editarIssue(request, idIssue):
    
    if request.method == 'GET':
        # obten el issue con este id
        issue = Issue.objects.get(id=idIssue)
        # modifica los atributos del issue
        if request.GET.get('asunto'):
            # crea una actividad
            actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="asunto", usuario=request.user)
            actividad.save()
            issue.asunto = request.GET.get('asunto')
            issue.save()

        if request.GET.get('descripcion'):
            actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="descripcion", usuario=request.user)
            actividad.save()
            issue.descripcion = request.GET.get('descripcion')
            issue.save()


        puedo_asignar = False

        if issue.asignada == None :
            puedo_asignar = True
        elif request.GET.get('asignada') != issue.asignada.username and request.GET.get('asignada') != '':
            puedo_asignar = True
         

        if  puedo_asignar:
            if request.GET.get('asignada') == "sin asignar":
                if issue.asignada != None:
                    actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="desasignada", usuario=request.user)
                    actividad.save()
                issue.asignada = None
                issue.save()
            else:
                actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="asignada", usuario=request.user)
                actividad.save()
                username_asignado = request.GET.get('asignada')
                user = User.objects.get(username=username_asignado)
                issue.asignada = user
                issue.save()

        actividades = Actividad_Issue.objects.filter(issue_id=idIssue)
        return render(request, 'mostrarIssue.html', {'issue': issue, 'actividades' : actividades})
    return render(request, 'editarIssue.html', {'error' : 'No se ha podido actualizar el issue'})
