from django.shortcuts import render, redirect
from polls.models import Issue, Actividad_Issue, Equipo, Miembro_Equipo, Watcher
from django.contrib.auth.models import User
import datetime
from django.db.models import Q, Max
from django.db import models


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
            vigilantes = request.GET.get('vigilante')

            if asignado == "sin asignar":
                asignado = None
            else:
                usuario_asignado = User.objects.get(username=asignado)
            
            if vigilantes == "sin asignar":
                vigilantes = None
            else:
                usuario_vigilante = User.objects.get(username=vigilantes)
                
            
            issue = Issue(asunto=asunto, descripcion=descripcion, creador=creador, asignada=usuario_asignado)
            issue.save()
            issue.addWatcher(usuario_vigilante)
        
            actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="creada", usuario=request.user)
            actividad.save()

            watching = Watcher(issue=issue, usuario=creador)
            watching.save()
        
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

#Eliminar un vigilante de un issue
def eliminarVigilante(request, idIssue, idWatcher):
    issue = Issue.objects.get(id=idIssue)
    usuario = User.objects.get(id=idWatcher)
    issue.removeWatcher(usuario)
    watching = Watcher.objects.filter(issue=issue, usuario=usuario)
    watching.delete()
    return redirect('mostrarIssue', idIssue=idIssue)

def mostrarUsuariosParaAñadir(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)

    return render(request, 'form_addWatchers.html', {'issues': issue, 'equipos' : equipos, 'equipo' : miembro_equipo, 'usuarios' : usuarios})

def agregarVigilante(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    usuario = User.objects.get(id=request.POST.get('vigilante'))

    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)
    
    if issue.vigilant.filter(id=usuario.id).exists():
        mensaje_error = "El usuario ya es un watcher."
        context = {"mensaje_error": mensaje_error, 'issues': issue, 'equipos': equipos, 'equipo': miembro_equipo, 'usuarios': usuarios}
        return render(request, 'form_addWatchers.html', context)
    
    issue.addWatcher(usuario)
    watching = Watcher(issue=issue, usuario=usuario)
    watching.save()

    mensaje_exito = "Watcher añadido correctamente."
    context = {"mensaje_exito": mensaje_exito, 'issues': issue, 'equipos': equipos, 'equipo': miembro_equipo, 'usuarios': usuarios}
    return render(request, 'form_addWatchers.html', context)


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

def filtrar_issues(request):
    filtro = request.GET.get('filtro')
    opciones = request.GET.get('opciones')

    # Verificamos si se seleccionó algún filtro
    if filtro:
        # Filtramos por el tipo de filtro seleccionado
        if filtro == 'status':
            issues = Issue.objects.filter(status=opciones, deleted=False)
        elif filtro == 'assignee':
            issues = Issue.objects.filter(associat=opciones, deleted=False)
        elif filtro == 'tag':
            issues = Issue.objects.filter(tag=opciones, deleted=False)
        elif filtro == 'priority':
            issues = Issue.objects.filter(priority=opciones, deleted=False)
        elif filtro == 'assign_to':
            issues = Issue.objects.filter(asignada=opciones, deleted=False)
        elif filtro == 'created_by':
            issues = Issue.objects.filter(creador=opciones, deleted=False)
        else:
            # Si no se reconoce el filtro, retornamos un error
            issues = None
    else:
        # Si no se seleccionó ningún filtro, mostramos todos los issues
        issues = Issue.objects.filter(deleted=False)

    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)
    return render(request, 'filterIssues.html', {'issues' : issues, 'equipos' : equipos, 'equipo' : miembro_equipo, 'usuarios' : usuarios})


def search_issues(request):
    query = request.GET.get('q')
    if query:
        results = Issue.objects.filter(Q(asunto__icontains=query) | Q(descripcion__icontains=query), deleted=False)
    else:
        results = Issue.objects.filter(deleted=False)
    
    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)

    return render(request, 'main.html', {'issues': results, 'equipos' : equipos, 'equipo' : miembro_equipo, 'usuarios' : usuarios})

def ordenar_issues(request):
    issue_ids = request.GET.get('issue_ids', '')
    issue_ids = [int(id) for id in issue_ids.split(',') if id]
    issues = Issue.objects.filter(id__in=issue_ids)

    orden = request.GET.get('orden', 'issue')
    orden_dir = request.GET.get('orden_dir')

    if orden_dir == 'asc':
        orden = '' + orden
    else:
        orden = '-' + orden

    if orden == 'modified' or orden == '-modified':
        max_fecha_actividad = Max('actividad_issue__fecha')
        order_by_field = 'max_fecha_actividad' if orden_dir == 'desc' else '-max_fecha_actividad'

        issues = issues.annotate(
            max_fecha_actividad=max_fecha_actividad
        ).order_by(order_by_field)

    else:
        issues = issues.order_by(orden)

    issues = issues.filter(deleted=False)

    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)

    return render(request, 'main.html', {'issues': issues, 'equipos': equipos, 'equipo': miembro_equipo, 'usuarios': usuarios})

