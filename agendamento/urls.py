# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    ProfissionalCreateView, AgendamentoCreateView, ProfissionalListView, 
    AgendamentoListView, ServicoCreateView, ServicoListView, 
    ProfissionalDeleteView, AgendamentoDeleteView, ServicoDeleteView,
    IndexView, AgendamentoUpdateView, ProfissionalUpdateView, 
    ServicoUpdateView, admin_dashboard, GetHorariosDisponiveisView, ChatbotView, ChatbotResponseView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
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
    path('accounts/login/', auth_views.LoginView.as_view(next_page='index'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('horarios-disponiveis/', GetHorariosDisponiveisView.as_view(), name='horarios-disponiveis'),
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('chatbot/response/', ChatbotResponseView.as_view(), name='chatbot_response'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)