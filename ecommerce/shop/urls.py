from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderItemViewSet, OrderViewSet, ReviewViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'reviews',ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]