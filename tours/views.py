from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import BikeRoute, Booking, Tour
from .forms import GalleryForm, TourForm, BikeRouteForm, BookingForm
from django.contrib.auth.decorators import login_required
from .utils import handle_uploaded_file


"""
This section deals with the static loaded pages. 
For general viewing of a page add them here
"""


def index(request):
    """
    Endpoint: /
    Description: Home page with general infomation
    """
    return render(request, 'homepage.html')


@login_required(login_url='/login/')
def tours(request):
    """
    Endpoint: /tours
    Description: Page to view alll of the tours that are saved
    """
    tours = get_list_or_404(
        Tour.objects.prefetch_related('tour_routes', 'tour_bookings').all()
    )
    
    context = {
        'tours':tours
    }

    
    return render(request, 'tours.html', context)


@login_required(login_url='/login/')
def bookings(request):
    """
    Endpoint: /bookings
    Description: Page to show all the bookings saved
    """
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})


@login_required(login_url='/login/')
def bikeroutes(request):
    """
    Endpoint: /bikeroutes
    Description: Page to show all the bike routes saved 
    """
    bikeroutes = BikeRoute.objects.all()
    return render(request, 'bikeroutes.html', {'bikeroutes': bikeroutes})


@login_required(login_url='/login/')
def gallery(request):
    """
    Endpoint: /gallery
    Description: Where the users can store photos
    """
    return render(request, 'gallery.html')


"""
This section deals with urls for the forms and dynamic pages where users can add data
"""


@login_required(login_url='/login/')
def new_tour(request):
    """
    Endpoint: /tours/new
    Description: Where new tours can be added
    """
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            tour = Tour.objects.create(
                tour_name=form.cleaned_data['tour_name'],
                tour_date=form.cleaned_data['tour_date'],
            )
            tour.tour_routes.set(form.cleaned_data['tour_routes'])
            tour.tour_bookings.set(form.cleaned_data['tour_bookings'])
            return redirect('tours')
    else:
        form = TourForm()
    return render(request, 'forms/tour_form.html', {'form': form})


@login_required(login_url='/login/')
def new_route(request):
    """
    Endpoint: /bikeroutes/new
    Description: Where new routes can be added 
    """
    if request.method == 'POST':
        form = BikeRouteForm(request.POST)
        if form.is_valid():
            BikeRoute.objects.create(
                route_name=form.cleaned_data['route_name'],
                route_distance=form.cleaned_data['route_distance'],
                route_link=form.cleaned_data['route_link'],
            )
            return redirect('bikeroutes')
    else:
        form = BikeRouteForm()
    return render(request, 'forms/route_form.html', {'form': form})


@login_required(login_url='/login/')
def new_booking(request):
    """
    Endpoint: /bookings/new
    Description: Where new bookings can be added 
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            Booking.objects.create(
                booking_name=form.cleaned_data['booking_name'],
                booking_cost=form.cleaned_data['booking_cost'],
                booking_date=form.cleaned_data['booking_date'],
            )
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'forms/booking_form.html', {'form': form})


@login_required(login_url='/login/')
def new_photo(request):
    """
    Endpoint: /gallery/new
    Description: Where new photos can be added 
    """
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('gallery')
    else:
        form = GalleryForm()
    return render(request, 'upload.html', {'form': form})