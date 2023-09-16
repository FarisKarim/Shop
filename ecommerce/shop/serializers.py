from rest_framework import serializers
from .models import Product, Review, Category, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = 'user.username')
    class Meta:
        model = Order
        fields = ['id', 'total_price','created_at','user']


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source = 'product.name')
    order = serializers.StringRelatedField()
    class Meta:
        model = OrderItem
        fields = ['id','product','quantity', 'order']
