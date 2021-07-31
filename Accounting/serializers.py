from rest_framework import serializers
from .models import AccountingData


class AccountingDataSerializer(serializers.ModelSerializer):
    class Meta:    
        model = AccountingData
        fields = '__all__'











