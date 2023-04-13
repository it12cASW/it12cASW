from polls.consts import status, prioridades, status_order
from django.shortcuts import render, redirect, redirect, redirect
from polls.models import Issue, Actividad_Issue, Equipo, Miembro_Equipo, Watcher, Comentario, Deadline
from django.contrib.auth.models import User
import datetime
from django.db.models import Q, Max, Case, When, Value
from django.db import models
from django.db.models import Case, CharField, Value, When


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

        return render(request, 'crearIssue.html', {'usuarios' : usuarios, "prioridades" : prioridades, 'status': status})
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
            usuario_asignado = None


            if asignado == "sin asignar":
                asignado = None
            else:
                if User.objects.filter(username=asignado).exists():
                    usuario_asignado = User.objects.get(username=asignado)
                else:
                    usuario_asignado = None
                    #return render(request, 'crearIssue.html', {'error' : 'El usuario asignado no existe', 'usuarios' : usuarios})

                        
            if vigilantes == "sin asignar":
                usuario_vigilante = None
            else:
                usuario_vigilante = User.objects.get(username=vigilantes)
                
            # Prioridad
            prioridad = None
            if request.GET.get('prioridad') != "ninguna":
                prioridad = request.GET.get('prioridad')

            
            issue = Issue(asunto=asunto, descripcion=descripcion, creador=creador, asignada=usuario_asignado, prioridad=prioridad)
            issue.save()
            if usuario_vigilante:
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
    
    motivo = ""
    if issue.deadline != None:
        deadline = Deadline.objects.get(issue_id=idIssue)
        if deadline.motivo != None:
            motivo = deadline.motivo
    
    return render(request, 'mostrarIssue.html', {'issue': issue, 'creador' : creador, 'actividades' : actividades, 'motivo' : motivo, 'comments': issue.comments.all()})

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
        return render(request, 'editarIssue.html', {'issue': issue, 'creador' : creador, 'usuarios' : aux, "prioridades" : prioridades, 'status': status})

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

        # Prioridad
        
        if request.GET.get('prioridad') != "ninguna":
            issue.prioridad = request.GET.get('prioridad')
            issue.save()

        if request.GET.get('status') and request.GET.get('status') != issue.status:
            issue.status = request.GET.get('status')
            issue.save()

        actividades = Actividad_Issue.objects.filter(issue_id=idIssue)
        return render(request, 'mostrarIssue.html', {'issue': issue, 'actividades' : actividades, 'comments': issue.comments.all()})
    return render(request, 'editarIssue.html', {'error' : 'No se ha podido actualizar el issue'})

def pantallaAddDeadline(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    motivo = ""
    if issue.deadline is not None:
        deadline = Deadline.objects.get(issue_id=idIssue)
        motivo = deadline.motivo
    return render(request, 'form_addDeadline.html', {'error' : "", 'issue' : issue, 'motivo' : motivo})


def addDeadline(request, idIssue):
    try:
        issue = Issue.objects.get(id=idIssue)
    except Issue.DoesNotExist:
        return render(request, 'form_addDeadline.html', {'error' : "La issue no existe"})

    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        if fecha == '':
            return render(request, 'form_addDeadline.html', {'error' : "La fecha no puede estar vacía", 'issue' : issue})
        elif issue.deadline is not None:
            return render(request, 'form_addDeadline.html', {'error' : "La issue ya tiene una deadline", 'issue' : issue})
        else:
            motivo = request.POST.get('motivo')
            issue.setDeadline(fecha, motivo)
            issue.save()
            return render(request, 'form_addDeadline.html', {'error' : "El deadline se ha añadido correctamente", 'issue' : issue, 'motivo' : motivo})
    
    return render(request, 'form_addDeadline.html', {'issue' : issue})

def eliminarDeadline(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    issue.deadline = None
    issue.save()
    deadline = Deadline.objects.get(issue=issue)
    deadline.delete()
    return render(request, 'form_addDeadline.html', {'issue': issue,  'error' : "La deadline ha sido eliminada correctamente" })


def addComment(request, idIssue):
    if request.method == 'GET':
        if request.GET.get('contenido') != '':
            autor = User.objects.get(id=request.user.id)
            contenido = request.GET.get('contenido')
            issue = Issue.objects.get(id=idIssue)

            comment = Comentario(autor=autor, contenido=contenido, issue=issue)
            comment.save()
            actividades = Actividad_Issue.objects.filter(issue_id=idIssue)
            return render(request, 'mostrarIssue.html', {'issue': issue, 'actividades' : actividades, 'comments': issue.comments.all()})

        else:
            return render(request, 'añadirComment.html', {'error' : "El contenido no puede estar vacío"})
    return render(request, 'añadirComment.html', {'error' : "El comentario se ha añadido correctamente"})


def eliminarComment(request, idComment):

    comment = Comentario.objects.get(id=idComment)
    # modifica el atributo 'deleted' a True
    comment.deleted = True
    comment.save()
    return render(request, 'eliminarComment.html', { 'comentario': comment })

def bulkInsertView(request):
    return render(request, 'bulkInsert.html')

def bulkInsert(request):
    if request.method == 'GET':
        if request.GET.get('newIssues') != '':

            for asunto in request.GET.get('newIssues').splitlines():
                issue = Issue(asunto=asunto, descripcion="", creador=request.user)
                issue.save()

                actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="creada", usuario=request.user)
                actividad.save()

            return render(request, 'bulkInsert.html')

        else:
            return render(request, 'bulkInsert.html', {'error': 'El esta vacio'})

def bloquearIssue(request, idIssue):

    if request.method == 'GET':
        issue = Issue.objects.get(id=idIssue)
        issue.blocked = True
        issue.reason_blocked = request.GET.get('razon') if request.GET.get('razon') != '' else None
        issue.save()

        actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="bloqueada",
                                    usuario=request.user)
        actividad.save()

        return redirect('mostrarIssue', idIssue=idIssue)

def desbloquearIssue(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    issue.blocked = False
    issue.reason_blocked = None
    issue.save()

    actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="desbloqueada",
                                usuario=request.user)
    actividad.save()
    return redirect('mostrarIssue', idIssue=idIssue)

def quieroBloquear(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    return render(request, 'bloquearIssue.html', {'issue': issue})

def filtrar_issues(request):
    filtro = request.GET.get('filtro')
    estados = request.GET.get('estados')
    prioridades_sel = request.GET.get('prioridades')
    assigned_to = request.GET.get('assigned_to')
    creado_por = request.GET.get('creado_por')
    asignados = request.GET.get('asignados')
    # Verificamos si se seleccionó algún filtro
    if filtro:
        # Filtramos por el tipo de filtro seleccionado
        if filtro == 'status':
            issues = Issue.objects.filter(status=estados, deleted=False)
        elif filtro == 'assignee':
            issues = Issue.objects.filter(asignada=asignados, deleted=False)
        elif filtro == 'priority':
            issues = Issue.objects.filter(prioridad=prioridades_sel, deleted=False)
        elif filtro == 'created_by':
            issues = Issue.objects.filter(creador=creado_por, deleted=False)
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
    return render(request, 'filterIssues.html', {'issues' : issues, 'equipos' : equipos, 'equipo' : miembro_equipo, 'usuarios' : usuarios, 'prioridades': prioridades, 'status': status})

def search_issues(request):
    query = request.GET.get('q')

    if query:
        results = Issue.objects.filter(Q(asunto__icontains=query) | Q(descripcion__icontains=query), deleted=False)
    else:
        results = Issue.objects.filter(deleted=False)
    
    equipos = Equipo.objects.all()
    equipo_usuario = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)

    return render(request, 'main.html', {'issues': results, 'equipos' : equipos, 'equipo' : equipo_usuario, 'usuarios' : usuarios})

def ordenar_issues(request):
    issue_ids = request.GET.get('issue_ids', '')
    issue_ids = [int(id) for id in issue_ids.split(',') if id]
    issues = Issue.objects.filter(id__in=issue_ids, deleted=False)

    orden = request.GET.get('orden', 'issue')
    orden_dir = request.GET.get('orden_dir')

    if orden_dir == 'asc':
        orden = '' + orden
    else:
        orden = '-' + orden

    if orden == 'modified' or orden == '-modified':
        max_fecha_actividad = Max('actividades__fecha')
        order_by_field = 'max_fecha_actividad' if orden_dir == 'desc' else '-max_fecha_actividad'

        issues = issues.annotate(
            max_fecha_actividad=max_fecha_actividad
        ).order_by(order_by_field)
    elif orden == 'prioridad' or orden == '-prioridad':
        issues = issues.annotate(
            priority_order=Case(
                When(prioridad='baja', then=Value(3)),
                When(prioridad='media', then=Value(2)),
                When(prioridad='alta', then=Value(1)),
                output_field=models.IntegerField(),
                default=Value(4),
            )
        ).order_by('priority_order' if orden_dir == 'asc' else '-priority_order')
    elif orden == 'status' or orden == '-status':
        status_order_case = Case(
            *[When(status=value, then=Value(position)) for position, value in enumerate(status_order.keys())],
            output_field=CharField(),
        )
        issues.order_by(status_order_case)
        if orden_dir == 'desc':
            issues = issues[::-1]
    else:
        issues = issues.order_by(orden)


    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)

    return render(request, 'main.html', {'issues': issues, 'equipos': equipos, 'equipo': miembro_equipo, 'usuarios': usuarios})

