from .views import BlogViewSet, ProductViewSet, PostObjectViewSet, PostCreateViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path


urlpatterns = [
    path('posts/', PostObjectViewSet.as_view(), name='post-list'),
    path('posts/create/', PostCreateViewSet.as_view(), name='post-create'),
]


router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('blog', BlogViewSet, basename='blog')


urlpatterns += router.urls
