from rest_framework import viewsets
from contas.api import serializers
from contas import models

class contasViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.contasSerializer
  queryset = models.Contas.objects.all()