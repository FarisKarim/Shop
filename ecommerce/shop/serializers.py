from rest_framework import serializers
from .models import Product, Review, Category, Order, OrderItem


class ProductSerializer:
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer:
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer:
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer:
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer:
    class Meta:
        model = OrderItem
        fields = '__all__'
