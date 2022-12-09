from django.db import models
from uuid import uuid4

import accounts
from accounts.views import CustomAuthToken

# Create your models here.
class Contas(models.Model):
  id_conta = models.UUIDField(primary_key = True, default=uuid4, editable=False)
  tipo_conta = models.CharField(max_length=50)
  nome_conta = models.CharField(max_length=255)
  saldo_inicial = models.FloatField()
  id_user = models.CharField(max_length=255)
  