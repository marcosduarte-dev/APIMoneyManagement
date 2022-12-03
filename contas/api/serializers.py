from rest_framework import serializers
from contas import models

class contasSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Contas
    fields = '__all__'