from rest_framework import serializers
from .models import Product, Blog, Posts


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['created_at', 'updated_at'] 


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        exclude = ['created_at', 'updated_at'] 