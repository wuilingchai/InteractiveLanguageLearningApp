from rest_framework import serializers
from .models import LearningData

class LearningDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningData
        fields = ['id', 'user', 'data']
