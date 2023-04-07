from django.shortcuts import render
from polls.models import Issue
from django.contrib.auth.models import User


def pantallaCrearIssue(request):
    return render(request, 'crearIssue.html')


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

def mostrarIssue(request, idIssue):
    # obten el issue con este id
    issue = Issue.objects.get(id=idIssue)
    creador = User.objects.get(id=issue.creador.id)
    return render(request, 'mostrarIssue.html', {'issue': issue, 'creador' : creador })

def eliminarIssue(request, idIssue):
    issue = Issue.objects.get(id=idIssue)
    # modifica el atributo 'deleted' a True
    issue.deleted = True
    issue.save()
    return render(request, 'eliminarIssue.html', { 'issue': issue })