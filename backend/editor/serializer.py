from rest_framework import serializers
from .models import Document, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class DocumentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, source='tags', queryset=Tag.objects.all()
    )

    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'created', 'updated', 'tags', 'tag_ids']
