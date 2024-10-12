# models.py
from django.db import models
from datetime import timedelta, datetime

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='profissionais/', blank=True, null=True)
    disponibilidade = models.JSONField(default=dict)  # Novo campo para armazenar a disponibilidade

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagem = models.ImageField(upload_to='servicos/', default='servicos/sem-imagem.jpg')
    duracao = models.DurationField(default=timedelta(hours=1))

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
