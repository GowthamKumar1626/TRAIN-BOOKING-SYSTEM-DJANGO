from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = UserModel
        fields = ["id", "username", "email", "first_name", "last_name", "mobile_number", "is_admin"]
        
    def get_is_admin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = UserModel
        fields = ["id", "username", "email", "first_name", "last_name", "mobile_number", "is_admin", "token"]
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        
        for key, value in serializer.items():
            data[key] = value

        return data