from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'categoria', 'status', 'defeito_relatado', 'previsao_conserto', 'tecnico_responsavel']
