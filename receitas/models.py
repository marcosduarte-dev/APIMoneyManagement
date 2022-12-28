from uuid import uuid4
from django.db import models

class Receitas(models.Model):
  id_receita = models.UUIDField(primary_key = True, default=uuid4, editable=False)
  id_conta = models.CharField(max_length=50)
  valor = models.FloatField()
  data_lancamento = models.DateField()
  data_receita = models.DateField()