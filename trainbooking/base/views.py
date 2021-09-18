from django.contrib.auth.hashers import make_password

from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.serializers import UserSerializer
from base.serializers import MyTokenObtainPairSerializer, UserSerializer, UserSerializerWithToken


UserModel = get_user_model()

@api_view(["GET"])
def get_all_users(request):
    try:
        users = UserModel.objects.all()
        data = UserSerializer(users, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return Response({"detail": str(error)}, status=status.HTTP_400_BAD_REQUEST)


# LOGIN VIEW

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# REGISTER VIEW

@api_view(["POST"])
def registerUser(request):
    data = request.data
    try:
        user = UserModel.objects.create(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            username = data.get('username'),
            email = data.get("email"),
            mobile_number = data.get('mobile_number'),
            password = make_password(data["password"])
        )
        serializer = UserSerializerWithToken(user)
        return Response(serializer.data)
    except Exception as error:
        message = {"details": f"{error}"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# UPDATE USER DATA

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    mobile_number = data.get('mobile_number')

    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if email:
        user.email = email
    if password:
        user.password = make_password(password)
    if mobile_number:
        user.mobile_number = mobile_number

    user.save()

    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)