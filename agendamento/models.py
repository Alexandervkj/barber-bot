# models.py
from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    telefone = models.CharField(max_length=15)
    confirmacao = models.BooleanField(default=False)

    class Meta:
        unique_together = ('profissional', 'data', 'horario')

    def __str__(self):
        return f"{self.nome} - {self.servico} com {self.profissional} em {self.data} às {self.horario}"
    
class Servico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome