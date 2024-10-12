# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, UpdateView, View
from django.urls import reverse_lazy
from .models import Profissional, Agendamento, Servico
from .forms import ProfissionalForm, AgendamentoForm, ServicoForm, AgendamentoSearchForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime, date, timedelta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .utils import is_horario_disponivel

class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

    def form_valid(self, form):
        servico = form.cleaned_data['servico']
        data = form.cleaned_data['data']
        horario = form.cleaned_data['horario']
        profissional = form.cleaned_data['profissional']

        if not is_horario_disponivel(servico, data, horario, profissional):
            form.add_error('horario', 'O horário selecionado não está disponível.')
            return self.form_invalid(form)

        return super().form_valid(form)

class ProfissionalCreateView(LoginRequiredMixin, CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'profissional_form.html'
    success_url = reverse_lazy('profissional_list')

    def form_valid(self, form):
        messages.success(self.request, 'Profissional adicionado com sucesso!')
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

@login_required
def admin_dashboard(request):
    forms = {
        'profissional_form': ProfissionalForm,
        'servico_form': ServicoForm,
    }

    if request.method == 'POST':
        for form_name, form_class in forms.items():
            if form_name in request.POST:
                form = form_class(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('admin_dashboard')
    else:
        context = {form_name: form_class() for form_name, form_class in forms.items()}
        context.update({
            'profissionais': Profissional.objects.all(),
            'servicos': Servico.objects.all(),
        })
        return render(request, 'admin_dashboard.html', context)

class GetHorariosDisponiveisView(View):
    def get(self, request, *args, **kwargs):
        servico_id = request.GET.get('servico')
        profissional_id = request.GET.get('profissional')
        data_str = request.GET.get('data')
        data = datetime.strptime(data_str, '%Y-%m-%d').date()
        servico = get_object_or_404(Servico, id=servico_id)
        profissional = get_object_or_404(Profissional, id=profissional_id)
        horarios = self.get_horarios_disponiveis(servico, data, profissional)
        horarios_str = [str(horario) for horario in horarios]
        return JsonResponse({'horarios': horarios_str})

    def get_horarios_disponiveis(self, servico, data, profissional):
        horarios = []
        hora_inicio = timedelta(hours=8)  # Exemplo: horário de início às 8h
        hora_fim = timedelta(hours=18)  # Exemplo: horário de término às 18h
        duracao = servico.duracao

        while hora_inicio + duracao <= hora_fim:
            if not Agendamento.objects.filter(data=data, horario=hora_inicio, profissional=profissional).exists():
                horarios.append(hora_inicio)
            hora_inicio += duracao

        return horarios

class ChatbotView(TemplateView):
    template_name = 'chatbot.html'