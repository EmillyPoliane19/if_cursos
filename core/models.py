from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    data = models.DateField('Data de nascimento')
    cpf = models.CharField('CPF', max_length=11, unique=True) 
    telefone = models.CharField('Telefone', max_length=11) #mudei para charfield
    matricula = models.CharField('Matrícula', max_length=14)

    #USERNAME_FIELD: str = 'cpf'  ESTAVA ERRADO
    USERNAME_FIELD = 'cpf'  #Este é o formato correto