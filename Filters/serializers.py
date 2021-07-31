from rest_framework import serializers
from .models import FilterData


class FilterDataSerializer(serializers.ModelSerializer):
    class Meta:
    
        model = FilterData
        fields = '__all__'











