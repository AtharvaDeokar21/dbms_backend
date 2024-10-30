from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FarmerProfileViewSet,
    CropInfoViewSet,
    FertilizerPesticideInfoViewSet,
    SalesViewSet,
    RegisterUserView,
    LoginView,
    ManageCropViewSet, 
    GrowsViewSet, 
    LogoutView
)

router = DefaultRouter()
router.register(r'farmers', FarmerProfileViewSet)
router.register(r'crops', CropInfoViewSet)
router.register(r'fertilizers', FertilizerPesticideInfoViewSet)
router.register(r'market-data', SalesViewSet)
router.register(r'managecrop', ManageCropViewSet)
router.register(r'grows', GrowsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
