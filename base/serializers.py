from rest_framework import serializers
from .models import LearningData, DialogData

class LearningDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningData
        fields = ['id', 'user', 'data']

class DialogDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DialogData
        fields = ['id', 'user', 'data']