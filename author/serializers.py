from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['surname', 'name', 'patronymic']