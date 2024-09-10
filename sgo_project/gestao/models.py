from django.db import models

class NotificacaoAcidente(models.Model):
    setor = models.CharField(max_length=100)
    responsavel_setor = models.CharField(max_length=100)
    descricao_atividade = models.TextField()
    descricao_risco = models.TextField()
    data = models.DateField()
    hora = models.TimeField()
    nome_colaborador = models.CharField(max_length=100)
    sugestao_melhorias = models.TextField(blank=True, null=True)
    parecer_seguranca = models.TextField(blank=True, null=True)
    prazo_resolucao = models.CharField(max_length=100, blank=True, null=True)
    risco_neutralizado = models.CharField(
        max_length=20,
        choices=[('sim', 'Sim'), ('nao', 'Não'), ('parcialmente', 'Parcialmente')]
    )
    metodo_neutralizacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Notificação de acidente de {self.nome_colaborador} em {self.data}"
