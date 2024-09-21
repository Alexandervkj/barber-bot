# agendamento/urls.py
from django.urls import path
from .views import ProfissionalCreateView, AgendamentoCreateView, ProfissionalListView, AgendamentoListView, ServicoCreateView, ServicoListView

urlpatterns = [
    path('profissional/add/', ProfissionalCreateView.as_view(), name='profissional_add'),
    path('agendamento/add/', AgendamentoCreateView.as_view(), name='agendamento_add'),
    path('profissionais/', ProfissionalListView.as_view(), name='profissional_list'),
    path('agendamentos/', AgendamentoListView.as_view(), name='agendamento_list'),
    path('servico/add/', ServicoCreateView.as_view(), name='servico_add'),
    path('servicos/', ServicoListView.as_view(), name='servico_list'),
]