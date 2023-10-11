from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet,GenericProduct

router = DefaultRouter()

router.register('products/', ProductViewSet, basename='products')

urlpatterns = [
    path('productview/', GenericProduct.as_view()),
        path('productview/<int:pk>/', GenericProduct.as_view()),


]


