from rest_framework import serializers
from .models import ItemType

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ['type_name', 'description']
