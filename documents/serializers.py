from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'uploaded_at','is_draft', 'editable_by', 'land_owner_agreed', 'land_seller_agreed']
        read_only_fields = ['uploaded_at', 'owner', 'land_owner_agreed', 'land_seller_agreed']
