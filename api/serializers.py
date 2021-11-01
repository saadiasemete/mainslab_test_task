from rest_framework import serializers
from .models import SentMessageData

class SentMessageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentMessageData
        fields = '__all__'
        read_only_fields = ['id', 'created_at']