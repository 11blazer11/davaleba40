from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .models import Product, Blog, Posts
from .serializers import ProductSerializer, BlogSerializer, PostsSerializer
from .throttle import PostOnlyThrottle #custom aris

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle, PostOnlyThrottle]  

class PostObjectViewSet(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    throttle_classes = [ScopedRateThrottle] 
    throttle_scope = 'posts_list' 

class PostCreateViewSet(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    throttle_classes = [ScopedRateThrottle]  
    throttle_scope = 'posts_create'