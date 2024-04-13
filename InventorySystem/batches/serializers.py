from rest_framework import serializers
from .models import Batch

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batch_code', 'date_received', 'quantity', 'item']
