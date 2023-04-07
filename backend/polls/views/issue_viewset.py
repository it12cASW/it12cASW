from django.shortcuts import render
from polls.models import Issue, Actividad_Issue
from django.contrib.auth.models import User
import datetime




# Mostrar pantalla de creación de un issue
def pantallaCrearIssue(request):
    return render(request, 'crearIssue.html')

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

        actividades = Actividad_Issue.objects.filter(issue_id=idIssue)
        return render(request, 'mostrarIssue.html', {'issue': issue, 'actividades' : actividades})
    return render(request, 'editarIssue.html', {'error' : 'No se ha podido actualizar el issue'})
