
from django.db import models
# Importación de los modelos 
from django.contrib.auth.models import User


class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=50, default='')
    descripcion = models.CharField(max_length=200, default='')
    #creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_creadas')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_creadas')
    associat = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_associado', null=True)
    vigilant = models.ManyToManyField(User,  related_name='issues_vigiladas', default='', null=True)
    deleted = models.BooleanField(default=False)


# Creame un modelo Actividad_Issue que guarde informacion de las modificaciones que se hacen a un issue con una foreign key que contenga el id del issue y otra del creador
class Actividad_Issue(models.Model):
    id = models.AutoField(primary_key=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE) # id de la issue
    creador = models.ForeignKey(User, on_delete=models.CASCADE) # id del creador
    fecha = models.DateTimeField(auto_now_add=True) # fecha de publicacion del cambio
    tipo = models.CharField(max_length=1000, default='') # tipo de cambio
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_usuario') # id del usuario que ha hecho el cambio

    def __str__(self):
        return self.descripcion

    def setAtributos(self, issue, creador, descripcion):
        self.issue = issue
        self.creador = creador
        self.descripcion = descripcion

    def guardarEnBD(self):
        self.save()

    def existeEnDB(self):
        return Actividad_Issue.objects.filter(issue=self.issue).exists()

