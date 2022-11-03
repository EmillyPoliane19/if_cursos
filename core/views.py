from django.shortcuts import render


#Página Inicial
def home(request):
    return render(request,'pagina_inicial.html')

# Create your views here.
