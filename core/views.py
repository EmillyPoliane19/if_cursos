from tkinter.tix import Form
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Modalidade, Area, Cursos
from .forms import ModalidadeForm, AreaForm, CursoForm,UsuarioCreationForm

#Página Inicial__________________________________________________________________________________________________________
def home(request):
    return render(request,'Página_inicial.html')

#Página do curso__________________________________________________________________________________________________________
def pagina_curso(request):
    return render(request,'pagina_curso.html')

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
        return render(request, 'registration/login.html')

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
    return render(request,'registration/geral.html') 
#Comentários
@login_required
def comentario(request):
    return render(request, 'comentarios.html')


#Cadastro de curso
#@login_required
def cadastro(request):
  return render(request, 'curso/cadastro_curso.html')


#Páginas do site________________________________________________________________________________________________________
#Áreas
def area(request):
    return render (request, 'areas/area.html')
#Modalidades
def modalidade(request):
    return render (request, 'modalidades/modalidade.html')
#fitros
def filtro(request):
    listar_cursos = Cursos.objects.all()
    listar_areas = Area.objects.all()
    palavra = ''
    areas_selecionadas = []
    if request.POST:
        palavra = request.POST['palavra']
        if request.POST.get('area_selecao', None):
            areas_selecionadas = request.POST.getlist('area_selecao')
            listar_cursos = Cursos.objects.filter(nome__contains = palavra).filter(area__id__in = areas_selecionadas)
        else:
            listar_cursos = Cursos.objects.filter(nome__contains = palavra)
    
    contexto = {
        'listar_cursos': listar_cursos,
        'palavra': palavra,
        'listar_areas': listar_areas,
        'areas_selecionadas': areas_selecionadas
    }

    return render(request,'Filtro_cursos.html', contexto)


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
    return render(request, 'modalidades/modalidade.html', contexto)

def cadastro_modalidade(request):
    form = ModalidadeForm(request. POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('modalidade')

    contexto = {
        'form_modalidade': form
    }
    return render(request, 'modalidades/cadastro_modalidade.html', contexto)

def editar_modalidades(request, id):
    modalidade = Modalidade.objects.get(pk=id)
    
    form = ModalidadeForm(request.POST or None, request.FILES or None ,instance=modalidade)
   
    if form.is_valid():
        form.save()
        return redirect('modalidade')
    
    contexto = {
        'form_modalidade': form
    }

    return render(request, 'modalidades/cadastro_modalidade.html', contexto)

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
    return render(request, 'areas/area.html', contexto)

def cadastrar_areas(request):
    form = AreaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('area')

    contexto = {
        'form_area': form
    }
    return render(request, 'areas/cadastro_area.html', contexto)

def editar_areas(request, id):
    area = Area.objects.get(pk=id)
    
    form = AreaForm(request.POST or None, request.FILES or None ,instance=area)
   
    if form.is_valid():
        form.save()
        return redirect('area')
    
    contexto = {
        'form_area': form
    }

    return render(request, 'areas/cadastro_area.html', contexto)

def remover_areas(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('area')

#CRUD Cursos_____________________________________________________________________________________________________________
def listar_cursos(request):
    cursos = Cursos.objects.all()
    contexto = {
        'todos_cursos': cursos
    }
    return render(request, 'curso/cursos.html', contexto)

def cadastrar_cursos(request):
    form = CursoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('cursos')

    contexto = {
        'form_cursos': form
    }
    return render(request, 'curso/cadastro_curso.html', contexto)

def editar_cursos(request, id):
    cursos = Cursos.objects.get(pk=id)
    
    form = CursoForm(request.POST or None, request.FILES or None ,instance=cursos)
   
    if form.is_valid():
        form.save()
        return redirect('cursos')
    
    contexto = {
        'form_cursos': form
    }

    return render(request, 'curso/cadastro_curso.html', contexto)

def remover_cursos(request, id):
    cursos = Cursos.objects.get(pk=id)
    cursos.delete()
    return redirect('cursos')