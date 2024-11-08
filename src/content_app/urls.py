from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet, basename='content')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = router.urls 
