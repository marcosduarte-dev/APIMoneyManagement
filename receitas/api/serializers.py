from rest_framework import serializers
from receitas import models

class receitasSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Receitas
    fields = '__all__'