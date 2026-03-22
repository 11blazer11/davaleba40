from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .models import Product, Blog, Post
from .serializers import ProductSerializer, BlogSerializer, PostSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    throttle_classes = [ScopedRateThrottle]  