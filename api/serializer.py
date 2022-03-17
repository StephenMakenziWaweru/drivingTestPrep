from rest_framework import serializers
from questions.models import Question
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    """Serializes a Question"""
    class Meta:
        model = Question
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """Serializes a User"""
    class Meta:
        model = User
        fields = ['id', 'username']
