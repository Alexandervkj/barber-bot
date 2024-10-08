# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    ProfissionalCreateView, AgendamentoCreateView, ProfissionalListView, 
    AgendamentoListView, ServicoCreateView, ServicoListView, 
    ProfissionalDeleteView, AgendamentoDeleteView, ServicoDeleteView,
    IndexView, AgendamentoUpdateView, ProfissionalUpdateView, DiaFuncionamentoCreateView, 
    HorarioFuncionamentoCreateView, DiaFuncionamentoListView, HorarioFuncionamentoListView, 
    ServicoUpdateView, HorarioFuncionamentoDeleteView, HorarioFuncionamentoUpdateView,
    DiaFuncionamentoUpdateView, DiaFuncionamentoDeleteView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profissional/add/', ProfissionalCreateView.as_view(), name='profissional_add'),
    path('agendamento/add/', AgendamentoCreateView.as_view(), name='agendamento_add'),
    path('profissionais/', ProfissionalListView.as_view(), name='profissional_list'),
    path('agendamentos/', AgendamentoListView.as_view(), name='agendamento_list'),
    path('servico/add/', ServicoCreateView.as_view(), name='servico_add'),
    path('servicos/', ServicoListView.as_view(), name='servico_list'),
    path('profissional/delete/<int:pk>/', ProfissionalDeleteView.as_view(), name='profissional_delete'),
    path('agendamento/delete/<int:pk>/', AgendamentoDeleteView.as_view(), name='agendamento_delete'),
    path('servico/delete/<int:pk>/', ServicoDeleteView.as_view(), name='servico_delete'),
    path('agendamento/edit/<int:pk>/', AgendamentoUpdateView.as_view(), name='agendamento_edit'),
    path('profissional/edit/<int:pk>/', ProfissionalUpdateView.as_view(), name='profissional_update'),
    path('servicos/edit/<int:pk>/', ServicoUpdateView.as_view(), name='servico_update'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('horarios-funcionamento/', HorarioFuncionamentoListView.as_view(), name='horario_funcionamento_list'),
    path('horarios-funcionamento/add/', HorarioFuncionamentoCreateView.as_view(), name='horario_funcionamento_add'),
    path('horarios-funcionamento/<int:pk>/edit/', HorarioFuncionamentoUpdateView.as_view(), name='horario_funcionamento_update'),
    path('horarios-funcionamento/<int:pk>/delete/', HorarioFuncionamentoDeleteView.as_view(), name='horario_funcionamento_delete'),
    path('dias-funcionamento/', DiaFuncionamentoListView.as_view(), name='dia_funcionamento_list'),
    path('dias-funcionamento/add/', DiaFuncionamentoCreateView.as_view(), name='dia_funcionamento_add'),
    path('dias-funcionamento/<int:pk>/edit/', DiaFuncionamentoUpdateView.as_view(), name='dia_funcionamento_update'),
    path('dias-funcionamento/<int:pk>/delete/', DiaFuncionamentoDeleteView.as_view(), name='dia_funcionamento_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)