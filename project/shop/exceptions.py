from rest_framework import status
from rest_framework.exceptions import APIException


class NotAuthorized(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {"message": 'Login failed'}
    default_code = 'login_failed'


class EmptyCart(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = {"message": 'Cart is empty'}
    default_code = 'empty_cart'
