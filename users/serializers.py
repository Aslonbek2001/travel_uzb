from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


    


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'phone', 'user_role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    



class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                return user
        raise serializers.ValidationError("Incorrect Credentials")