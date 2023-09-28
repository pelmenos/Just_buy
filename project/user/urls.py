from django.urls import path
from .views import *


urlpatterns = [
    path('signup', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='knox_logout'),
]
