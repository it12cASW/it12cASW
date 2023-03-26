from django.db import models


# Create your models here.
# crea una clase user que guarde toda su infromacion
class User(models.Model):
    # crea un nuevo campo para la edad que sea por defecto 5
    nombre = models.CharField(max_length=50, default='')
    apellidos = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nombre

    def setAtributos(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def guardarEnBD(self):
        self.save()

    def existeEnDB(self):
        return User.objects.filter(email=self.email).exists()

    # crea una funcion que devuelva el usuario con el email que le pasas
    @staticmethod
    def getUsuarioConEmail(email):
        return User.objects.filter(email=email)
