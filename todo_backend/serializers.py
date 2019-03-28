from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Todo

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'title',
            'body',
            'slug',
        ]

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'user',
            'title',
            'body',
            'slug',
            'todo_done',
            'pub_date',
        ]

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'user',
            'title',
            'body',
            'slug',
            'pub_date',
        ]
