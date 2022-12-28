import genericpath
from rest_framework import viewsets
from contas.api import serializers
from contas import models
from django_filters.rest_framework import DjangoFilterBackend

class contasViewSet(viewsets.ModelViewSet):
  queryset = models.Contas.objects.all()
  serializer_class = serializers.contasSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id_user']