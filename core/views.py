from tkinter.tix import Form
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Modalidade, Area
from .forms import ModalidadeForm, AreaForm, UsuarioCreationForm

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
    form = UsuarioCreationForm (request.POST or None)
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
#Cadastro de area
def cadastro_area(request):
    return render(request, 'cadastro_area.html')

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
        username='admin4',
        email='admin@email.com',
        cpf='12345',
        nome='Administrador',
        matricula='222222',
        telefone='84999999999',
        password='admin123',
        data='2001-01-01',
        is_superuser=True)
    user.save()
    return redirect('home')

#CRUD Modalidades________________________________________________________________________________________________________
def listar_modalidades(request):
    modalidade = Modalidade.objects.all()
    contexto = {
        'todas_modalidade': modalidade
    }
    return render(request, 'modalidade.html', contexto)

def cadastro_modalidade(request):
    form = ModalidadeForm(request. POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('modalidade')

    contexto = {
        'form_modalidade': form
    }
    return render(request, 'cadastro_modalidade.html', contexto)

def editar_modalidades(request, id):
    modalidade = Modalidade.objects.get(pk=id)
    
    form = ModalidadeForm(request.POST or None, request.FILES or None ,instance=modalidade)
   
    if form.is_valid():
        form.save()
        return redirect('modalidade')
    
    contexto = {
        'form_modalidade': form
    }

    return render(request, 'cadastro_modalidade.html', contexto)

def remover_modalidades(request, id):
    modalidade = Modalidade.objects.get(pk=id)
    modalidade.delete()
    return redirect('modalidade')


#CRUD Area________________________________________________________________________________________________________
def listar_areas(request):
    area = Area.objects.all()
    contexto = {
        'todas_areas': area
    }
    return render(request, 'area.html', contexto)

def cadastrar_areas(request):
    form = AreaForm(request. POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('area')

    contexto = {
        'form_area': form
    }
    return render(request, 'cadastro_area.html', contexto)

def editar_areas(request, id):
    area = Area.objects.get(pk=id)
    
    form = AreaForm(request.POST or None, request.FILES or None ,instance=area)
   
    if form.is_valid():
        form.save()
        return redirect('area')
    
    contexto = {
        'form_area': form
    }

    return render(request, 'cadastro_area.html', contexto)

def remover_areas(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('area')