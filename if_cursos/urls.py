"""if_cursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import editar_areas, home, geral, listar_areas, registro
from core.views import comentario, cursos, cadastro_usuario, listar_modalidades,listar_cursos, filtro
from core.views import cadastro_usuario, cadastro_modalidade,cadastrar_areas,cadastrar_cursos
from core.views import remover_areas, remover_modalidades, editar_modalidades, editar_cursos, remover_cursos
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    

    #Páginas usuario
    path('', home, name='home'),
    path('filtro/', filtro, name='filtro'), 

    #Páginas adm
    path('cursos/', cursos, name='cursos'),
    path('registro/', registro, name='registro'),
    path('geral/', geral, name='geral'),
    path('comentario/', comentario, name='comentario'),

    #CRUD Usuario
    path('cadastro_usuario/', cadastro_usuario),

    #CRUD Area
    path('area/', listar_areas, name='area'),
    path('cadastro_area/', cadastrar_areas, name='cadastro_area'),
    path('editar_areas/<int:id>/', editar_areas, name='editar_areas'),
    path('remover_areas/<int:id>/', remover_areas, name='remover_areas'),

    #CRUD Cursos
    path ('cursos/', listar_cursos, name='cursos'),
    path ('cadastro_cursos/', cadastrar_cursos, name='cadastrar_cursos'),
    path ('editar_cursos/<int:id>/', editar_cursos,name='editar_cursos'),
    path ('remover_cursos/<int:id>/', remover_cursos, name='remover_cursos'),

    #CRUD Modalidades
    path('modalidade/', listar_modalidades, name='modalidade'),
    path('cadastro_modalidade/', cadastro_modalidade, name='cadastro_modalidade'),
    path('editar_modalidades/<int:id>/', editar_modalidades, name='editar_modalidades'),
    path('remover_modalidades/<int:id>/', remover_modalidades, name='remover_modalidades'),
]
