from django.db import models

class FarmerProfile(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)

class CropInfo(models.Model):
    crop_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    estimated_yield = models.DecimalField(max_digits=10, decimal_places=2)
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
