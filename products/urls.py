from .views import BlogViewSet, ProductViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [

]

router = DefaultRouter()
router.register()


urlpatterns += router.urls
