from django.db import models

# Modelo de usuario


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # metodo que devuelva el nombre del usuario
    def getName(self):
        return self.name

    def register(self):
        self.save()

    def __str__(self):
        return self.name
