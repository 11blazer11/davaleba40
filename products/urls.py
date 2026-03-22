# from .views import 
from rest_framework.routers import SimpleRouter, DefaultRouter

urlpatterns = [

]

router = DefaultRouter()
router.register()


urlpatterns += router.urls
