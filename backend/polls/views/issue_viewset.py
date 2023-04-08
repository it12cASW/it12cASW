from django.shortcuts import render
from polls.models import Issue, Actividad_Issue, Equipo, Miembro_Equipo
from django.contrib.auth.models import User
import datetime




# Mostrar pantalla de creación de un issue
def pantallaCrearIssue(request):

    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)

    return render(request, 'crearIssue.html', {'usuarios' : usuarios})

# Crear un nuevo issue
def crearIssue(request):

    if request.method == 'GET':
        asunto = request.GET.get('asunto')
        descripcion = request.GET.get('descripcion')
        creador = User.objects.get(id=request.user.id)
        issue = Issue(asunto=asunto, descripcion=descripcion, creador=creador)
        issue.save()
        
        actividad = Actividad_Issue(issue=issue, creador=issue.creador, fecha=datetime.datetime.now(), tipo="creada", usuario=request.user)
        actividad.save()
        #associat = request.POST.get('associat')
        #vigilant = request.POST.get('vigilant'
    
        
    return render(request, 'crearIssue.html')

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

    # Si el miembro tiene equipo

    if Miembro_Equipo.objects.filter(miembro=creador):
        equipo = Miembro_Equipo.objects.filter(miembro=creador)[0].equipo
        miembros = Miembro_Equipo.objects.filter(equipo=equipo)
        aux = []
        for miembro in miembros:
            aux.append(miembro.miembro)
        return render(request, 'editarIssue.html', {'issue': issue, 'creador' : creador, 'usuarios' : aux })

    return render(request, 'editarIssue.html', {'issue': issue, 'creador' : creador })

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

        if request.GET.get('asignada'):
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

    if filtro == 'status':
        issues = Issue.objects.filter(status=opciones, deleted=False)

    elif filtro == 'assignee':
        assignee = request.GET.get('assignee')
        assignee = User.objects.get(username=opciones)
        # lógica para filtrar por asignado a
        issues = Issue.objects.filter(associat=assignee)        
    #falsta el filtro de tag
    elif filtro == 'priority':
        priority = request.GET.get('priority')
        # lógica para filtrar por prioridad
        issues = Issue.objects.filter(prioridad=opciones, deleted=False)

    elif filtro == 'assign_to':
        assign_to = request.GET.get('assign_to')
        assign_to = User.objects.get(username=opciones)

        issues = Issue.objects.filter(asignada=assign_to, deleted=False)

    elif filtro == 'created_by':
        assignee = request.GET.get('assignee')
        assignee = User.objects.get(username=opciones)

        issues = Issue.objects.filter(creador=assignee, deleted=False)
    else:
        # lógica si no se seleccionó ningún filtro
        issues = Issue.objects.filter(deleted=False)

    equipos = Equipo.objects.all()
    miembro_equipo = Miembro_Equipo.objects.filter(miembro=request.user.id)
    equipo = Miembro_Equipo.objects.filter(miembro=request.user)
    miebros = Miembro_Equipo.objects.filter(equipo=equipo[0].equipo)
    usuarios = []
    for miembro in miebros:
        usuarios.append(miembro.miembro)
    return render(request, 'filterIssues.html', {'issues' : issues, 'equipos' : equipos, 'equipo' : miembro_equipo, 'usuarios' : usuarios})
