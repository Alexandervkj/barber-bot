# forms.py
from django import forms
from .models import Profissional, Agendamento, Servico
from datetime import datetime, date, timedelta
from .utils import is_horario_disponivel

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'imagem', 'disponibilidade']

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
        self.fields['data'].widget.attrs.update({'min': date.today()})
        self.fields['data'].widget.attrs.update({'max': (date.today() + timedelta(days=45))})

    def clean(self):
        cleaned_data = super().clean()
        servico = cleaned_data.get('servico')
        data = cleaned_data.get('data')
        horario = cleaned_data.get('horario')
        profissional = cleaned_data.get('profissional')

        if servico and data and horario and profissional:
            if not is_horario_disponivel(servico, data, horario, profissional):
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
