from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'fio', 'password']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'fio', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('Password must contain 6 or more symbols ', code='authorization')
        return value

    def validate(self, attrs):
        user = self.create(attrs)
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(label='Email')
    password = serializers.CharField(label='Password', style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise AuthenticationFailed({'detail': 'Auth failed'})

        attrs['user'] = user
        return attrs
