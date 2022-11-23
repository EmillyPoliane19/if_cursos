from django.shortcuts import render
from django.contrib.auth import authenticate, login

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