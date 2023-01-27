from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    data = models.DateField('Data de nascimento')
    cpf = models.CharField('CPF', max_length=11, unique=True) 
    telefone = models.CharField('Telefone', max_length=11)
    matricula = models.CharField('Matrícula', max_length=14)
    username = models.CharField(null=True, max_length=50)

    USERNAME_FIELD = 'cpf'

class Modalidade(models.Model):
   nome = models.CharField('Nome', max_length=100)

class Area(models.Model):
   nome = models.CharField('Nome', max_length=100)
   def __str__(self):
      return self.nome


class Cursos(models.Model):
   nome = models.CharField('Nome', max_length=100)
   area = models.ForeignKey(Area,on_delete=models.PROTECT)