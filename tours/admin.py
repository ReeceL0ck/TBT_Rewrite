from django.contrib import admin

# Register your models here.
from .models import BikeRoute, Booking, Tour

admin.site.register(BikeRoute)
admin.site.register(Booking)
admin.site.register(Tour)
