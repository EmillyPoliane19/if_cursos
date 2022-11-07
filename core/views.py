from django.shortcuts import render

#Página Inicial
def home(request):
    return render(request,'Página_inicial.html')

# Create your views here.
