
from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = ['id','title','content','author','timestamp','status']
