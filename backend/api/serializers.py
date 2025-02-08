from rest_framework import serializers
from .models import Upload, Metadata

class UploadSerializer(serializers.ModelSerializer):
    """Serializer for handling file uploads."""
    
    class Meta:
        model = Upload
        fields = ['id', 'user', 'file', 'uploaded_at']


class MetadataSerializer(serializers.ModelSerializer):
    """Serializer for extracted metadata from URLs."""
    
    class Meta:
        model = Metadata
        fields = ['id', 'user', 'url', 'title', 'description', 'keywords', 'created_at']
