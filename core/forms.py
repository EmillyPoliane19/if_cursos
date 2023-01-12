from django.forms import ModelForm
from .models import Modalidade, Area, Usuario
from django.contrib.auth.forms import UserCreationForm

class ModalidadeForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome']


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['nome']


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['password1','password2','cpf','nome','data','telefone','matricula']
