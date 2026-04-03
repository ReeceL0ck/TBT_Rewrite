from django.contrib import admin

# Register your models here.
from .models import BikeRoute, Booking, Tour, Gallery

admin.site.register(BikeRoute)
admin.site.register(Booking)
admin.site.register(Tour)
admin.site.register(Gallery)