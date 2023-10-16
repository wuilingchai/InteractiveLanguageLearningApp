from rest_framework import serializers
from .models import Choices

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'
