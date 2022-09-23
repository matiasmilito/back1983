from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import Products
from api.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()


