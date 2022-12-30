from tkinter.tix import Form
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

#Página Inicial__________________________________________________________________________________________________________
def home(request):
    return render(request,'Página_inicial.html')

#Páginas de login e logout_______________________________________________________________________________________________
def login(request):
    return render(request,'registration/login.html')

def logout(request):
    logout(request)
    return redirect('home')

def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('geral')
        else:
            return redirect('login')
    else:
        return render(request, 'registration\login.html')

#Página de Cadastro________________________________________________________________________________________________________
def registro(request):
    form = UserCreationForm (request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'registration/Cadastro.html', contexto)

#Páginas do admin________________________________________________________________________________________________________
#Geral
@login_required
def geral(request):
    return render(request,'registration\geral.html') 
#Comentários
@login_required
def comentario(request):
    return render(request, 'comentarios.html')
#Cursos
@login_required
def cursos(request):
    return render(request, 'cursos.html')
#Cadastro de curso
@login_required
def cadastro(request):
    return render(request, 'cadastro_curso.html')


#Páginas do site________________________________________________________________________________________________________
#Áreas
def area(request):
    return render (request, 'area.html')
#Modalidades
def modalidade(request):
    return render (request, 'modalidade.html')
#fitros
def filtro(request):
    return render(request,'Filtro_cursos.html')


#Usuário________________________________________________________________________________________________________
#Model Usuário
def cadastro_usuario(request):
    user = Usuario.objects.create_user(
        username='admin',
        email='admin@email.com',
        cpf='1234',
        nome='Administrador',
        matricula='222222',
        telefone='84999999999',
        password='admin123',
        data='2001-01-01',
        is_superuser=True)
    user.save()
    return redirect('home')