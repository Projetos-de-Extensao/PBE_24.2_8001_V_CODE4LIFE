"""
URL configuration for streaming_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from content_app.views import ContentViewSet, UsuarioViewSet
from feedback_app.views import FeedbackViewSet
from member_app.views import ConviteViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet, basename='content')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'convites', ConviteViewSet, basename='convite')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]