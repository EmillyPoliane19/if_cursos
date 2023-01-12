from django.forms import ModelForm
from .models import Modalidade, Area

class ModalidadeForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome']


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['nome']