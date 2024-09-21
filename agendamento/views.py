# views.py
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Profissional, Agendamento, Servico
from .forms import ProfissionalForm, AgendamentoForm, ServicoForm
from django.views.generic import TemplateView

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

class ProfissionalDeleteView(DeleteView):
    model = Profissional
    template_name = 'profissional_confirm_delete.html'
    success_url = reverse_lazy('profissional_list')

class AgendamentoDeleteView(DeleteView):
    model = Agendamento
    template_name = 'agendamento_confirm_delete.html'
    success_url = reverse_lazy('agendamento_list')

class ServicoDeleteView(DeleteView):
    model = Servico
    template_name = 'servico_confirm_delete.html'
    success_url = reverse_lazy('servico_list')

class IndexView(TemplateView):
    template_name = 'index.html'