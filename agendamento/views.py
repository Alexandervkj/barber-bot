# views.py
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Profissional, Agendamento, Servico
from .forms import ProfissionalForm, AgendamentoForm, ServicoForm

class ProfissionalCreateView(CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'profissional_form.html'
    success_url = reverse_lazy('profissional_list')

class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

class ProfissionalListView(ListView):
    model = Profissional
    template_name = 'profissional_list.html'
    context_object_name = 'profissionais'

class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'agendamento_list.html'
    context_object_name = 'agendamentos'

class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servico_list')

class ServicoListView(ListView):
    model = Servico
    template_name = 'servico_list.html'
    context_object_name = 'servicos'