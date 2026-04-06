
from django.contrib import admin
from django.urls import path, include
from tours import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "TBT Admin"
admin.site.site_title = "TBT Admin Portal"
admin.site.index_title = "Welcome to TBT AdminPortal"

urlpatterns = [ 
    path('U2FsdGVkX1ctHhTkRbj69RCkG9F7vA9Mbl5qOvnm2Y/', admin.site.urls),
    path('', include("user_login.urls")),
    path('', views.index, name='index'),
    path('tours/', views.tours, name='tours'),
    path('bookings/', views.bookings, name='bookings'),
    path('bikeroutes/', views.bikeroutes, name='bikeroutes'),
    path('gallery/', views.gallery, name='gallery'),
    path('profile/', views.profile, name='profile'),
    
    path('tours/new',views.new_tour, name='add_tour'),
    path('bikeroutes/new',views.new_route, name='add_route'),
    path('bookings/new',views.new_booking, name='add_booking'),
    path('gallery/new',views.new_photo, name='add_photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
