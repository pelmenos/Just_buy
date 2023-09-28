from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('cart/', GetCartView.as_view()),
    path('cart/<int:product_id>', CartProductView.as_view()),
    path('order/', OrderView.as_view()),
]
