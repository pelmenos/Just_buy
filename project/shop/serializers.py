from rest_framework import serializers
from .models import Product, Cart, Order


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product
    """
    class Meta:
        model = Product
        fields = '__all__'


class ProductForCartSerializer(serializers.ModelSerializer):
    """
    Serializer for Product when it called by Cart
    """
    _incr = 0
    id = serializers.SerializerMethodField()
    product_id = serializers.IntegerField(source='id')

    def get_id(self, obj):
        self._incr += 1
        return self._incr

    class Meta:
        model = Product
        fields = ['id', 'product_id', 'name', 'description', 'price']


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for Cart
    """
    products = ProductForCartSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['products']


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order
    """
    class Meta:
        model = Order
        fields = ['id', 'products', 'order_price']
