from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializer import ProductSerializer
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer

    queryset = Product.objects.all()

   

    def perform_create(self, serializer):
        return super().perform_create(serializer)
