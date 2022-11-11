from django.shortcuts import render

#Página Inicial
def home(request):
    return render(request,'Página_inicial.html')

def filtro(request):
    return render(request,'Filtro_cursos.html')

def login(request):
    return render(request,'login.html')
# Create your views here.
