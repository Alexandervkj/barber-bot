# forms.py
from django import forms
from .models import Profissional, Agendamento, Servico, DiaFuncionamento, HorarioFuncionamento

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'imagem']

class AgendamentoForm(forms.ModelForm):
    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), empty_label="Selecione um serviço")
    profissional = forms.ModelChoiceField(queryset=Profissional.objects.all(), empty_label="Selecione um profissional")

    class Meta:
        model = Agendamento
        fields = ['nome', 'servico', 'profissional', 'data', 'horario', 'telefone', 'confirmacao']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco', 'imagem']

class AgendamentoSearchForm(forms.Form):
    nome = forms.CharField(required=False, label='Nome')
    servico = forms.CharField(required=False, label='Serviço')
    profissional = forms.CharField(required=False, label='Profissional')

class DiaFuncionamentoForm(forms.ModelForm):
    class Meta:
        model = DiaFuncionamento
        fields = ['dia']

class HorarioFuncionamentoForm(forms.ModelForm):
    class Meta:
        model = HorarioFuncionamento
        fields = ['dia', 'horario_inicio', 'horario_fim']