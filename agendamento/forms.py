# forms.py
from django import forms
from .models import Profissional, Agendamento, Servico

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome']

class AgendamentoForm(forms.ModelForm):
    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), empty_label="Selecione um serviço")
    profissional = forms.ModelChoiceField(queryset=Profissional.objects.all(), empty_label="Selecione um profissional")

    class Meta:
        model = Agendamento
        fields = ['nome', 'servico', 'profissional', 'data', 'horario', 'telefone', 'confirmacao']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome']