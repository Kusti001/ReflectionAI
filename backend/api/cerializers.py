from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = [
            'id', 'title', 'content', 'date', 'created_at', 'updated_at','ai_summary',
            'sentiment_score', 'emotions', 'ai_processed', 'ai_processed_at'
        ]
        read_only_fields = [
            'id', 'created_at', 'updated_at', 'sentiment_score', 'ai_summary',
            'emotions', 'ai_processed', 'ai_processed_at'
        ]