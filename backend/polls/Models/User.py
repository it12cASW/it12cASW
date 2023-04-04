from django.db import models


class User(models.Model):
    # crea un nuevo campo para la edad que sea por defecto 5
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