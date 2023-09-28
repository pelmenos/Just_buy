from django.contrib.auth import login, user_logged_out

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView

from .serializers import RegisterUserSerializer, LoginUserSerializer
from shop.permissions import CustomIsAuthenticated


class RegisterView(KnoxLoginView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response = super().post(request, format=None)
        return Response({'user_token': response.data['token']}, status=status.HTTP_200_OK)


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response = super().post(request, format=None)
        return Response({'user_token': response.data['token']}, status=status.HTTP_200_OK)


class LogoutView(KnoxLogoutView):
    permission_classes = (CustomIsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        return Response({'message': 'logout'}, status=status.HTTP_200_OK)
