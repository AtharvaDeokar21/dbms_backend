from rest_framework import viewsets
from .models import FarmerProfile
from .serializers import FarmerProfileSerializer

class FarmerProfileViewSet(viewsets.ModelViewSet):
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileSerializer
