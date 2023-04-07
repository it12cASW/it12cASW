from django.shortcuts import render
from polls.models import Issue
from django.contrib.auth.models import User




# Mostrar pantalla de creación de un issue
def pantallaCrearIssue(request):
    return render(request, 'crearIssue.html')

# Crear un nuevo issue
def crearIssue(request):

    if request.method == 'GET':
        asunto = request.GET.get('asunto')
        descripcion = request.GET.get('descripcion')

        print("ASUNTO: " + asunto + " DESCRIPCION: " + descripcion)

        creador = User.objects.get(id=request.user.id)
        print("creador ok")
        issue = Issue(asunto=asunto, descripcion=descripcion, creador=creador)
        print("issue ok")
        issue.save()
        print("Se ha creado el issue")
        #associat = request.POST.get('associat')
        #vigilant = request.POST.get('vigilant'
       
    else:
        print("No ha funcionaod")
    return render(request, 'crearIssue.html')

# Mostrar la información del issue dado su id
def mostrarIssue(request, idIssue):
    # obten el issue con este id
    issue = Issue.objects.get(id=idIssue)
    creador = User.objects.get(id=issue.creador.id)
    return render(request, 'mostrarIssue.html', {'issue': issue, 'creador' : creador })

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
            print("hay asunto")
            issue.asunto = request.GET.get('asunto')
            issue.save()

        if request.GET.get('descripcion'):
            print("hay descripcion")
            issue.descripcion = request.GET.get('descripcion')
            issue.save()

        print("ASUNTO: " + issue.asunto + " DESCRIPCION: " + issue.descripcion)
        return render(request, 'mostrarIssue.html', {'issue': issue})
    return render(request, 'editarIssue.html', {'error' : 'No se ha podido actualizar el issue'})
