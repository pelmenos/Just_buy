from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .exceptions import EmptyCart
from .models import Product, Cart, CartProduct, Order, OrderProduct
from .permissions import IsAdminOrReadOnly, CustomIsAuthenticated
from .serializers import ProductSerializer, CartSerializer, OrderSerializer
from .utils import GetSomething


class ProductList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView, GetSomething):
    permission_classes = [IsAdminOrReadOnly]

    def patch(self, request, pk, format=None):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_product(pk)
        product.delete()
        return Response({'message': "Product removed"}, status=status.HTTP_200_OK)


class GetCartView(APIView):
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        cart = Cart.objects.select_related('user').get(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartProductView(APIView, GetSomething):
    permission_classes = [CustomIsAuthenticated]

    def post(self, request, product_id):
        product = self.get_product(product_id)
        cart = Cart.objects.get(user=request.user)
        CartProduct.objects.create(cart=cart, product=product)
        return Response({"message": "Product add to cart"}, status=status.HTTP_201_CREATED)

    def delete(self, request, product_id):
        cart = Cart.objects.get(user=request.user)
        product = self.get_product_by_inCart_id(cart, product_id)
        cp = CartProduct.objects.filter(cart=cart, product=product).first()
        CartProduct.delete(cp)
        return Response({'message': "Item removed from cart"}, status=status.HTTP_200_OK)


class OrderView(APIView):
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user)

        if not cart.products:
            raise EmptyCart()

        for product in cart.products.all():
            OrderProduct.objects.create(order=order, product=product)
            order.order_price += product.price
        order.save()
        cart.products.clear()

        return Response({'order_id': order.id, 'message': "Order is processed"}, status=status.HTTP_201_CREATED)
