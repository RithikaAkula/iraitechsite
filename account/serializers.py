from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import status
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'phone']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    phone = PhoneNumberField()
    
    id = serializers.ReadOnlyField()

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)
        phone = data.get('phone', None)
        if email is None:
            raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)

        if password is None:
            raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password, phone=phone)


        if user is None:
            raise serializers.ValidationError(status.HTTP_401_UNAUTHORIZED)

        if user.phone != data.get('phone'):
            raise serializers.ValidationError(status.HTTP_401_UNAUTHORIZED)

        return {
            'id': user.id,
            'email': user.email,
            'phone':user.phone,
        }
        