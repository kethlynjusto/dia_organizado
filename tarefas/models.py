from django.db import models


class Tarefa(models.Model):
    OPCOES_STATUS = (
        ('concluído', 'Concluído'),  # o primeiro é do banco de dados e o segundo é o que aparecerá na app
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),

    )

    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('não urgente', 'Não Urgente'),
    )

    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIA, default='importante')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS, default='pendente')

