from django.db import models

# Importación de los modelos 
from polls.Models.User import User




class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=50, default='')
    descripcion = models.CharField(max_length=200, default='')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_creadas')
    associat = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_associado')
    vigilant = models.ManyToManyField(User,  related_name='issues_vigiladas')
    deleted = models.BooleanField(default=False)


