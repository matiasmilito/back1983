from django.urls import path, include
from rest_framework import routers

from api.views import ProductsViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]