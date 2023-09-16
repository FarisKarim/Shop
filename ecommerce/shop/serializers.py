from rest_framework import serializers
from .models import Product, Review, Category, Order, OrderItem
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    category= serializers.SlugRelatedField(slug_field='name', queryset = Category.objects.all())
    class Meta:
        model = Product
        fields = ['id','name','description','stock','price','category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only=True)
    user_display = serializers.CharField(source='user.username', read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all(), write_only=True)
    product_display = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Review
        fields = ['id','rating','comment','title','created_at','user','user_display','product','product_display']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = 'user.username')
    class Meta:
        model = Order
        fields = ['id', 'total_price','created_at','user']


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')
    product_name = serializers.CharField(source='product.name', read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), write_only=True, source='order')
    order_display = serializers.CharField(source='order.__str__', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'product_name', 'quantity', 'order_id', 'order_display']
    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)