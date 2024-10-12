# utils.py
from datetime import datetime
from .models import Agendamento

def is_horario_disponivel(servico, data, horario, profissional):
    duracao = servico.duracao
    horario_fim = (datetime.combine(datetime.min, horario) + duracao).time()
    agendamentos = Agendamento.objects.filter(data=data, horario__lt=horario_fim, horario__gte=horario, profissional=profissional)
    return not agendamentos.exists()