from django import forms
from ezbook_admin.models import User, Company, Driver, Vehicle, Travel_Places, BookTravel, Booking


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'firstname',
            'middlename',
            'lastname',
            'age',
            'phone_number',
            'email',
        )
        labels = {
            'firstname': 'First Name',
            'middlename': 'Middle Name',
            'lastname': 'Last Name',
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'username',
            'name_company',
            'email',
            'phone_number',
        )
        labels = {
            'name_company': 'Company Name',
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = (
            'driver_fullname',
            'company_name',
        )
        labels = {
            'driver_fullname': 'Driver Full Name',
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = (
            'vehicle_plate',
            'vehicle_driver_id',
            'vehicle_capacity',
            'vehicle_type',
            'company_id'
        )
        labels = {
            'vehicle_driver_id': 'Vehicle Driver',
            'company_id': 'Company'
        }


class Travel_PlacesForm(forms.ModelForm):
    class Meta:
        model = Travel_Places
        fields = ('places',)
        labels = {
            'places': 'Place'
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'seat_number',
            'user_travel_id',
            'book_travel_id',
        )
        labels = {
            'user_travel_id': 'User',
            'book_travel_id': 'Travel Place',
        }


class BookTravelForm(forms.ModelForm):
    class Meta:
        model = BookTravel
        fields = (
            'vehicle_id',
            'place_from',
            'place_to',
            'available_travel_date',
            'available_travel_time',
            'company',
        )
        labels = {
            'vehicle_id': 'Vehicle',
            'available_travel_date': 'Travel date',
            'available_travel_time': 'Travel time',
        }
        widgets = {
            'available_travel_date': forms.DateInput(format="%m/%d/%Y", attrs={'type': 'date'}),
            'available_travel_time': forms.TimeInput(format="%H:%M", attrs={'type': 'time'})
        }
