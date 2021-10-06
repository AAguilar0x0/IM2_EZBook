from django.urls import path, re_path, include
from ezbook_admin import views

app_name = 'ezbook_admin'

urlpatterns = [
    path('', views.dashboard, name="index"),
    path('tables/', include([
        re_path(r'^users/(?P<successRemarks>.*)?',
                views.Users.as_view(), name='users'),
        re_path(r'^companies/(?P<successRemarks>.*)?',
                views.Companies.as_view(), name='companies'),
        re_path(r'^drivers/(?P<successRemarks>.*)?',
                views.Drivers.as_view(), name='drivers'),
        re_path(r'^vehicles/(?P<successRemarks>.*)?',
                views.Vehicles.as_view(), name='vehicles'),
        re_path(r'^travelplaces/(?P<successRemarks>.*)?', views.Travelplaces.as_view(),
                name='travelplaces'),
        re_path(r'^bookings/(?P<successRemarks>.*)?',
                views.Bookings.as_view(), name='bookings'),
        re_path(r'^availablebookings/(?P<successRemarks>.*)?', views.Availablebookings.as_view(),
                name='availablebookings'),
    ]))
]
