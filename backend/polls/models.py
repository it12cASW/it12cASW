from django.db import models
# Importación de los modelos 
from django.contrib.auth.models import User
from .consts import status, prioridades


# Clase issue
class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=50, default='')
    descripcion = models.CharField(max_length=200, default='')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_creadas')
    associat = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_associado', null=True)
    vigilant = models.ManyToManyField(User, related_name='issues_vigiladas')
    deleted = models.BooleanField(default=False)
    asignada = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_asignadas', null=True)
    blocked = models.BooleanField(default=False, null=True)
    reason_blocked = models.CharField(max_length=200, default='', null=True)
    deadline = models.DateTimeField(null=True)
    prioridad = models.CharField(max_length=100, default=None, null=True)
    status = models.CharField(max_length=100, default=None, null=True)

    # si se añade un nuevo watcher, se añade a la lista de watchers
    def addWatcher(self, user):
        self.vigilant.add(user)

    def removeWatcher(self, user):
        self.vigilant.remove(user)

    def setDeadline(self, fecha, motivo):
        self.deadline = fecha
        deadline = Deadline.objects.create(issue=self, deadline=fecha, motivo=motivo)
        deadline.save()
        self.save()

    def __str__(self):
        return f"{self.asunto} ({self.id})"


# Clase actividad_issue
class Actividad_Issue(models.Model):
    id = models.AutoField(primary_key=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='actividades')  # id de la issue
    creador = models.ForeignKey(User, on_delete=models.CASCADE)  # id del creador
    fecha = models.DateTimeField(auto_now_add=True)  # fecha de publicacion del cambio
    tipo = models.CharField(max_length=1000, default='')  # tipo de cambio
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='actividades_hechas')  # id del usuario que ha hecho el cambio

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


# Clase equipo
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default='', unique=True)
    descripcion = models.CharField(max_length=200, default='')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equipos_creados')


# clase miemrbo_equipo --> UN MIEBRO SOLO PUEDE PERTENECER A UN EQUIPO
class Miembro_Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    miembro = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    rol = models.CharField(max_length=50, default='')


# clase que almacene los usuarios y su imagen de perfil
class Imagen_Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    imagen = models.ImageField(upload_to='imagenes_perfil', null=True, blank=True)


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    deleted = models.BooleanField(default=False)


# clase que almacena los usuarios y las issues que observan
class Watcher(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watcher')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='whatched')

    def delete(self, *args, **kwargs):
        self.issue.removeWatcher(self.usuario)
        super(Watcher, self).delete(*args, **kwargs)


class Deadline(models.Model):
    id = models.AutoField(primary_key=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='deadlines')
    deadline = models.DateTimeField()
    motivo = models.CharField(max_length=200, default='')
