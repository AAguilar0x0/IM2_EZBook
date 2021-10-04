from django.urls import path, include
from ezbook_admin import views

app_name = 'ezbook_admin'

urlpatterns = [
    path('', views.dashboard, name="index"),
    path('tables/', include([
        path('users/', views.Users.as_view(), name='users'),
        path('companies/', views.Companies.as_view(), name='companies'),
        path('drivers/', views.Drivers.as_view(), name='drivers'),
        path('vehicles/', views.Vehicles.as_view(), name='vehicles'),
        path('travelplaces/', views.Travelplaces.as_view(),
             name='travelplaces'),
        path('bookings/', views.Bookings.as_view(), name='bookings'),
        path('availablebookings/', views.Availablebookings.as_view(),
             name='availablebookings'),
    ]))
]
