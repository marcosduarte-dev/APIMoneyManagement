from rest_framework import viewsets
from receitas.api import serializers
from receitas import models
from django_filters.rest_framework import DjangoFilterBackend

class receitasViewSet(viewsets.ModelViewSet):
  queryset = models.Receitas.objects.all()
  serializer_class = serializers.receitasSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id_conta', 'data_lancamento', 'data_receita']