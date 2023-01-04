from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    data = models.DateField('Data de nascimento')
    cpf = models.CharField('CPF', max_length=11, unique=True) 
    telefone = models.CharField('Telefone', max_length=11)
    matricula = models.CharField('Matrícula', max_length=14)
    

    USERNAME_FIELD = 'cpf'

class Modalidade(models.Model):
   id = models.CharField('Id', max_length=14, primary_key=True) 
   nome = models.CharField('Nome', max_length=100)