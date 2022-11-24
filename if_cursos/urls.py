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
from core.views import home,filtro, login, geral, comentario, cursos, cadastro, cadastro_usuario, area, modalidade
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('filtro/', filtro, name='filtro'),
    #path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('geral/', geral, name='geral'),
    path('login/', login, name='login'),
    path('comentario/', comentario, name='comentario'),
    path('cursos/', cursos, name='cursos'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('area/', area, name='area'),
     path('modalidade/', modalidade, name='modalidade'),
]
