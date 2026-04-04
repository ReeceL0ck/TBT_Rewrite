from tours.models import Tour, Booking, BikeRoute, Gallery
from datetime import date
from django import forms

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['photo','image_description']


class BikeRouteForm(forms.ModelForm):
    class Meta:
        model = BikeRoute
        fields = ['route_name', 'route_distance', 'route_link']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_name', 'booking_date', 'booking_cost']


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['tour_name', 'tour_date', 'tour_routes', 'tour_bookings']
