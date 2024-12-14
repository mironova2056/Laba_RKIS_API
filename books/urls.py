from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'authors', AthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]