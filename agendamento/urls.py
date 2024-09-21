# agendamento/urls.py
from django.urls import path
from .views import (
    ProfissionalCreateView, AgendamentoCreateView, ProfissionalListView, 
    AgendamentoListView, ServicoCreateView, ServicoListView, 
    ProfissionalDeleteView, AgendamentoDeleteView, ServicoDeleteView
)

urlpatterns = [
    path('profissional/add/', ProfissionalCreateView.as_view(), name='profissional_add'),
    path('agendamento/add/', AgendamentoCreateView.as_view(), name='agendamento_add'),
    path('profissionais/', ProfissionalListView.as_view(), name='profissional_list'),
    path('agendamentos/', AgendamentoListView.as_view(), name='agendamento_list'),
    path('servico/add/', ServicoCreateView.as_view(), name='servico_add'),
    path('servicos/', ServicoListView.as_view(), name='servico_list'),
    path('profissional/delete/<int:pk>/', ProfissionalDeleteView.as_view(), name='profissional_delete'),
    path('agendamento/delete/<int:pk>/', AgendamentoDeleteView.as_view(), name='agendamento_delete'),
    path('servico/delete/<int:pk>/', ServicoDeleteView.as_view(), name='servico_delete'),
]