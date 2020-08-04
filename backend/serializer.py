from rest_framework import serializers
from .models import martabak

class MartabakSerializer(serializers.ModelSerializer):
    class Meta:
        model = martabak
        fields = '__all__'