from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Document, Tag

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class DocumentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'created', 'updated', 'user', 'tags']
        read_only_fields = ['created', 'updated']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        document = Document.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            document.tags.add(tag)
        return document

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(**tag_data)
                instance.tags.add(tag)
        return instance 