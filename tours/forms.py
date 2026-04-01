from tours.models import Tour, Booking, BikeRoute
from datetime import date
from django import forms

class GalleryForm(forms.Form):
    image = forms.ImageField()
    description = forms.CharField(max_length=255)
    date_taken = forms.DateField(initial=date.today)


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
