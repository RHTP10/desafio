from django.db import models

# Create your models here
class Dono(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome