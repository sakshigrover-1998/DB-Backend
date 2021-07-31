from rest_framework import serializers
from .models import ExceptionType


class ExceptionTypeSerializer(serializers.ModelSerializer):
    class Meta:    
        model = ExceptionType
        fields = '__all__'











