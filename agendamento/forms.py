# forms.py
from django import forms
from .models import Profissional, Agendamento, Servico, DiaFuncionamento, HorarioFuncionamento
from datetime import datetime, date

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'imagem']

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'servico', 'profissional', 'data', 'horario', 'telefone']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servico'].queryset = Servico.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        servico = cleaned_data.get('servico')
        data = cleaned_data.get('data')
        horario = cleaned_data.get('horario')

        if servico and data and horario:
            duracao = servico.duracao
            horario_fim = (datetime.combine(date.min, horario) + duracao).time()

            # Verificar se o horário está disponível
            agendamentos = Agendamento.objects.filter(data=data, horario__lt=horario_fim, horario__gte=horario)
            if agendamentos.exists():
                raise forms.ValidationError("O horário selecionado não está disponível.")

        return cleaned_data

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco', 'imagem', 'duracao']

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