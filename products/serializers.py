from rest_framework import serializers
from .models import Product, Blog, Post


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['created_at', 'updated_at'] 


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['created_at', 'updated_at'] 