from rest_framework import serializers
from .models import AnonymBoard

class AnonymBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymBoard
        fields = ['title', 'content']