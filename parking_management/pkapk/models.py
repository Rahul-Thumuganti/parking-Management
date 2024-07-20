from django.db import models
from datetime import datetime

class Category(models.Model):
    parking_area_no = models.CharField(max_length=200, null=False, blank=False)
    vehicle_type = models.CharField(max_length=200, null=False, blank=False)
    vehicle_limit = models.CharField(max_length=200, null=False, blank=False)
    parking_charge = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True, null=False, blank=False)
    doc = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.vehicle_type


class add_vehicle(models.Model):
    vehicle_no = models.CharField(max_length=200, null=False, blank=False)
    vehicle_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    parking_area_no = models.CharField(max_length=200, null=False, blank=False)
    parking_charge = models.CharField(max_length=200,null=False, blank=False)  # Use FloatField with a default value
    status = models.BooleanField(default=True)
    arrival_time = models.DateTimeField(default=datetime.now, blank=True)




    def __str__(self):
        return self.parking_area_no






