from django.urls import path
from .views import ConviteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'convite', ConviteViewSet, basename='convite')

urlpatterns = router.urls
