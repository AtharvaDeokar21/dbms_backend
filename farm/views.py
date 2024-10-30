from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import FarmerProfileInfo, CropInfo, FertilizerPesticideInfo, Sales, ManageCrop, Grows
from .serializers import (
    FarmerProfileSerializer,
    CropInfoSerializer,
    FertilizerPesticideInfoSerializer,
    SalesSerializer,
    ManageCropSerializer, 
    GrowsSerializer, 
    UserSerializer
)


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Logged in successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


class FarmerProfileViewSet(viewsets.ModelViewSet):
    queryset = FarmerProfileInfo.objects.all()
    serializer_class = FarmerProfileSerializer
    permission_classes = [IsAuthenticated]


class CropInfoViewSet(viewsets.ModelViewSet):
    queryset = CropInfo.objects.all()
    serializer_class = CropInfoSerializer
    permission_classes = [IsAuthenticated]


class FertilizerPesticideInfoViewSet(viewsets.ModelViewSet):
    queryset = FertilizerPesticideInfo.objects.all()
    serializer_class = FertilizerPesticideInfoSerializer
    permission_classes = [IsAuthenticated]


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]

class ManageCropViewSet(viewsets.ModelViewSet):
    queryset = ManageCrop.objects.all()
    serializer_class = ManageCropSerializer
    permission_classes = [IsAuthenticated]

class GrowsViewSet(viewsets.ModelViewSet):
    queryset = Grows.objects.all()
    serializer_class = GrowsSerializer
    permission_classes = [IsAuthenticated]