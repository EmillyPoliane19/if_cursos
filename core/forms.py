from django.forms import ModelForm
from .models import Modalidade

class ModalidadeForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['id', 'nome']