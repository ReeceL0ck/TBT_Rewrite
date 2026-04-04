from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="./media")

# Create your models here.
"""
These are the models used in the application
"""
class BikeRoute(models.Model):
    route_name = models.CharField(max_length=100)
    route_distance = models.TextField()
    route_link = models.URLField()
    user         = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # Remove Default 1 once login system added 

    def __str__(self):
        return self.route_name

class Booking(models.Model):
    booking_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_cost = models.DecimalField(max_digits=10, decimal_places=2)
    user         = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # Remove Default 1 once login system added 

    def __str__(self):
        return self.booking_name

class Tour(models.Model):
    tour_name = models.CharField(max_length=100)
    tour_date = models.DateField()
    tour_routes = models.ManyToManyField(BikeRoute, related_name='tours', help_text="Hold alt to select multiple routes")
    tour_bookings = models.ManyToManyField(Booking, related_name='tours', help_text="Hold alt to select multiple routes")
    user         = models.ForeignKey(User, on_delete=models.CASCADE, default=1)# Remove Default 1 once login system added 
    

    def __str__(self):
        return self.tour_name

class Gallery(models.Model):
    image_description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="images",storage=fs)
    user         = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
