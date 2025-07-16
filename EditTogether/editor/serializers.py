from rest_framework import serializers
from .models import Document

# editor/serializers.py

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'content', 'updated_at', 'updated_by']