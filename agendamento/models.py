# models.py
from django.db import models
from datetime import timedelta

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='profissionais/', blank=True, null=True)  # Novo campo de imagem

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagem = models.ImageField(upload_to='servicos/', default='servicos/sem-imagem.jpg')
    duracao = models.DurationField(default=timedelta(hours=1))  # Adicionando o campo de duração

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    telefone = models.CharField(max_length=15)
    confirmacao = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.servico.nome} - {self.data} - {self.horario}"

class DiaFuncionamento(models.Model):
    DIAS_DA_SEMANA = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]
    dia = models.CharField(max_length=3, choices=DIAS_DA_SEMANA, unique=True)

    def __str__(self):
        return self.get_dia_display()

class HorarioFuncionamento(models.Model):
    dia = models.ForeignKey(DiaFuncionamento, on_delete=models.CASCADE)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        return f"{self.dia} - {self.horario_inicio} às {self.horario_fim}"

