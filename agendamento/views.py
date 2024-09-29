# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import Profissional, Agendamento, Servico, DiaFuncionamento, HorarioFuncionamento
from .forms import ProfissionalForm, AgendamentoForm, ServicoForm, AgendamentoSearchForm, DiaFuncionamentoForm, HorarioFuncionamentoForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django import forms

class ProfissionalCreateView(LoginRequiredMixin, CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'profissional_form.html'
    success_url = reverse_lazy('profissional_list')

    def form_valid(self, form):
        messages.success(self.request, 'Profissional adicionado com sucesso!')
        return super().form_valid(form)

class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['data'].widget = forms.Select(choices=self.get_dias_disponiveis())
        form.fields['horario'].widget = forms.Select(choices=self.get_horarios_disponiveis())
        return form

    def get_dias_disponiveis(self):
        dias = DiaFuncionamento.objects.all()
        return [(dia.dia, dia.get_dia_display()) for dia in dias]

    def get_horarios_disponiveis(self):
        horarios = HorarioFuncionamento.objects.all()
        return [(horario.horario_inicio, f"{horario.horario_inicio} às {horario.horario_fim}") for horario in horarios]

    def form_valid(self, form):
        messages.success(self.request, 'Agendamento adicionado com sucesso!')
        return super().form_valid(form)
    
class ServicoCreateView(LoginRequiredMixin, CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servico_list')

    def form_valid(self, form):
        messages.success(self.request, 'Serviço adicionado com sucesso!')
        return super().form_valid(form)

class IndexView(TemplateView):
    template_name = 'index.html'

class ProfissionalListView(LoginRequiredMixin, ListView):
    model = Profissional
    template_name = 'profissional_list.html'
    context_object_name = 'profissionais'

class ServicoListView(LoginRequiredMixin, ListView):
    model = Servico
    template_name = 'servico_list.html'
    context_object_name = 'servicos'

class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'agendamento_list.html'
    context_object_name = 'agendamentos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        servico = self.request.GET.get('servico')
        profissional = self.request.GET.get('profissional')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if servico:
            queryset = queryset.filter(servico__nome__icontains=servico)
        if profissional:
            queryset = queryset.filter(profissional__nome__icontains=profissional)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = AgendamentoSearchForm(self.request.GET)
        return context

class ProfissionalDeleteView(DeleteView):
    model = Profissional
    template_name = 'profissional_confirm_delete.html'
    success_url = reverse_lazy('profissional_list')

    def post(self, request, *args, **kwargs):
        messages.error(self.request, 'Profissional excluído com sucesso!')
        return super().post(request, *args, **kwargs)

class AgendamentoDeleteView(DeleteView):
    model = Agendamento
    template_name = 'agendamento_confirm_delete.html'
    success_url = reverse_lazy('agendamento_list')

    def post(self, request, *args, **kwargs):
        messages.error(self.request, 'Agendamento excluído com sucesso!')
        return super().post(request, *args, **kwargs)

class ServicoDeleteView(DeleteView):
    model = Servico
    template_name = 'servico_confirm_delete.html'
    success_url = reverse_lazy('servico_list')

    def post(self, request, *args, **kwargs):
        messages.error(self.request, 'Serviço excluído com sucesso!')
        return super().post(request, *args, **kwargs)

class AgendamentoUpdateView(UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Agendamento atualizado com sucesso!')
        return super().form_valid(form)

class ProfissionalUpdateView(UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'profissional_form.html'
    success_url = reverse_lazy('profissional_list')

    def form_valid(self, form):
        messages.success(self.request, 'Profissional atualizado com sucesso!')
        return super().form_valid(form)
    
class ServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servico_list')

    def form_valid(self, form):
        messages.success(self.request, 'Serviço atualizado com sucesso!')
        return super().form_valid(form)

class HorarioFuncionamentoListView(LoginRequiredMixin, ListView):
    model = HorarioFuncionamento
    template_name = 'horario_funcionamento_list.html'
    context_object_name = 'horarios'

class HorarioFuncionamentoCreateView(LoginRequiredMixin, CreateView):
    model = HorarioFuncionamento
    form_class = HorarioFuncionamentoForm
    template_name = 'horario_funcionamento_form.html'
    success_url = reverse_lazy('horario_funcionamento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Horário de funcionamento adicionado com sucesso!')
        return super().form_valid(form)

class HorarioFuncionamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = HorarioFuncionamento
    form_class = HorarioFuncionamentoForm
    template_name = 'horario_funcionamento_form.html'
    success_url = reverse_lazy('horario_funcionamento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Horário de funcionamento atualizado com sucesso!')
        return super().form_valid(form)

class HorarioFuncionamentoDeleteView(LoginRequiredMixin, DeleteView):    
    model = HorarioFuncionamento
    template_name = 'horario_funcionamento_confirm_delete.html'
    success_url = reverse_lazy('horario_funcionamento_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Horário de funcionamento excluído com sucesso!')
        return super().delete(request, *args, **kwargs)
    model = HorarioFuncionamento
    form_class = HorarioFuncionamentoForm
    template_name = 'horario_funcionamento_form.html'
    success_url = reverse_lazy('horario_funcionamento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Horário de funcionamento adicionado com sucesso!')
        return super().form_valid(form)

class DiaFuncionamentoListView(LoginRequiredMixin, ListView):
    model = DiaFuncionamento
    template_name = 'dia_funcionamento_list.html'
    context_object_name = 'dias'

class DiaFuncionamentoCreateView(LoginRequiredMixin, CreateView):
    model = DiaFuncionamento
    form_class = DiaFuncionamentoForm
    template_name = 'dia_funcionamento_form.html'
    success_url = reverse_lazy('dia_funcionamento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Dia de funcionamento adicionado com sucesso!')
        return super().form_valid(form)

class DiaFuncionamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = DiaFuncionamento
    form_class = DiaFuncionamentoForm
    template_name = 'dia_funcionamento_form.html'
    success_url = reverse_lazy('dia_funcionamento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Dia de funcionamento atualizado com sucesso!')
        return super().form_valid(form)

class DiaFuncionamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = DiaFuncionamento
    template_name = 'dia_funcionamento_confirm_delete.html'
    success_url = reverse_lazy('dia_funcionamento_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Dia de funcionamento excluído com sucesso!')
        return super().delete(request, *args, **kwargs)