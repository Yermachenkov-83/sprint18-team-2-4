from rest_framework import serializers
from .models import *
from author.serializers import AuthorListSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookListSerializer(serializers.ModelSerializer):
    authors = AuthorListSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')