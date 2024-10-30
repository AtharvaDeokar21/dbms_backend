from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import FarmerProfileInfo, CropInfo, FertilizerPesticideInfo, Sales, ManageCrop, Grows

User = get_user_model()

# User Serializer for Registration
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user

# FarmerProfile Serializer
class FarmerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfileInfo
        fields = '__all__'

# CropInfo Serializer
class CropInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropInfo
        fields = '__all__'

# FertilizerPesticideInfo Serializer
class FertilizerPesticideInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FertilizerPesticideInfo
        fields = '__all__'

# Sales Serializer
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

# ManageCrop Serializer
class ManageCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageCrop
        fields = '__all__'

# Grows Serializer
class GrowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grows
        fields = '__all__'