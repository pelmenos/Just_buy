from rest_framework.exceptions import NotFound

from .models import Product


class GetSomething:
    """
        This class allows you to take a single record from the database with error handling
    """
    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound(detail={'message': 'Not found'})

    def get_product_by_inCart_id(self, cart, product_id):
        try:
            return cart.products.all()[product_id - 1]
        except Exception:
            raise NotFound({'message': 'Not Found'})
