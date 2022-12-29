from django.shortcuts import render, redirect #Adicionei o redirect
from django.contrib.auth import authenticate, login
from .models import Usuario

#Página Inicial
def home(request):
    return render(request,'Página_inicial.html')

def filtro(request):
    return render(request,'Filtro_cursos.html')

def login(request):
    return render(request,'registration/login.html')

def perfil(request):
    return render(request,'perfil.html')

def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return redirect('login')
    else:
        return render(request, 'registration\login.html')

#Geral
def geral(request):
    return render(request,'geral.html') 

#Comentários
def comentario(request):
    return render(request, 'comentarios.html')

#Cursos
def cursos(request):
    return render(request, 'cursos.html')

#Cadastro de curso
def cadastro(request):
    return render(request, 'cadastro_curso.html')

#Áreas
def area(request):
    return render (request, 'area.html')

#Modalidades
def modalidade(request):
    return render (request, 'modalidade.html')

#Model Usuário
def cadastro_usuario(request):
    user = Usuario.objects.create_user(
        username='admin2',
        email='admin@email.com',
        cpf='222222222',
        nome='Administrador',
        matricula='222222',
        telefone='84999999999', #Adicionei telefone
        password='admin12345',
        data='2001-01-01', #mudei o formato
        is_superuser=True)
    user.save()
    return redirect('home')