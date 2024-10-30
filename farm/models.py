from django.db import models
from django.contrib.auth.models import User

class FarmerProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farmer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class CropInfo(models.Model):
    crop_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    estimated_yield = models.DecimalField(max_digits=10, decimal_places=2)
    farmer = models.ForeignKey(FarmerProfileInfo, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.crop_name} - Farmer ID: {self.farmer.farmer_id}"

class FertilizerPesticideInfo(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('Fertilizer', 'Fertilizer'), ('Pesticide', 'Pesticide')])
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    # crop = models.ForeignKey(CropInfo, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.item_name} - Type: {self.type}"

class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    crop = models.ForeignKey(CropInfo, on_delete=models.CASCADE)
    farmer = models.ForeignKey(FarmerProfileInfo, on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    earnings = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_sold = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateField()

    def _str_(self):
        return f"Market Data for Crop ID: {self.crop.crop_id}"

class Grows(models.Model):
    crop = models.ForeignKey(CropInfo, on_delete=models.CASCADE)
    farmer = models.ForeignKey(FarmerProfileInfo, on_delete=models.CASCADE)


class ManageCrop(models.Model):
    crop = models.ForeignKey(CropInfo, on_delete=models.CASCADE)
    product = models.ForeignKey(FertilizerPesticideInfo, on_delete=models.CASCADE)