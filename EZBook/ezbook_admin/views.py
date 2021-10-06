from django.shortcuts import redirect, render
from django.views.generic import View
from ezbook_admin.models import User, Company, Driver, Vehicle, Travel_Places, BookTravel, Booking
from ezbook_admin.forms import UserForm, CompanyForm, DriverForm, VehicleForm, Travel_PlacesForm, BookTravelForm, BookingForm
from datetime import date, datetime
from django.core import serializers
import json

# Create your views here.

base_title = 'EZBook Admin'


def dashboard(request):
    count = {
        "user_count": User.objects.all().count(),
        "bookings_count": Booking.objects.all().count(),
        "company_count": Company.objects.all().count(),
        "driver_count": Driver.objects.all().count(),
        "vehicle_count": Vehicle.objects.all().count(),
    }

    data = Booking.objects.raw(
        "SELECT 1 as id, COUNT(ID) as total, booking_date FROM heroku_edd82c657812381.booking group by booking_date")

    date = []
    num = []
    for i in data:
        date.append((i.booking_date))
        num.append(i.total)

    return render(request, 'ezbook_admin/index.html', {'title': f'{base_title} - Dashboard', 'count': count, 'date': json.dumps(date, cls=serializers.json.DjangoJSONEncoder), 'num': json.dumps(num)})


class Users(View):
    title = 'Users'

    def get(self, request, *args, **kwargs):
        form = UserForm()
        users = User.objects.all()
        return render(request, 'ezbook_admin/tables/users.html', {'title': f'{base_title} - {self.title}', 'users': users, 'form': form, 'successRemarks': kwargs['successRemarks']})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if request.POST.get('method') == 'delete':
            User.objects.filter(pk=request.POST.get('pk')).delete()
            return redirect('ezbook_admin:users',
                            successRemarks="User deleted successfully!")
        if form.is_valid():
            user = {
                'username': request.POST.get('username'),
                'firstname': request.POST.get('firstname'),
                'middlename': request.POST.get('middlename'),
                'lastname': request.POST.get('lastname'),
                'age': request.POST.get('age'),
                'phone_number': request.POST.get('phone_number'),
                'email': request.POST.get('email')
            }
            if request.POST.get('method') == 'insert':
                User(date_created=date.today(), **user).save()
                return redirect('ezbook_admin:users',
                                successRemarks="User added successfully!")
            elif request.POST.get('method') == 'update':
                User.objects.filter(pk=request.POST.get('pk')).update(**user)
                return redirect('ezbook_admin:users',
                                successRemarks="User updated successfully!")
        users = User.objects.all()
        return render(request, 'ezbook_admin/tables/users.html', {'title': f'{base_title} - {self.title}', 'users': users, 'form': form})


class Companies(View):
    title = 'Companies'

    def get(self, request, *args, **kwargs):
        form = CompanyForm()
        companies = Company.objects.all()
        return render(request, 'ezbook_admin/tables/companies.html', {'title': f'{base_title} - {self.title}', 'companies': companies, 'form': form, 'successRemarks': kwargs['successRemarks']})

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST)
        if request.POST.get('method') == 'delete':
            Company.objects.filter(pk=request.POST.get('pk')).delete()
            return redirect('ezbook_admin:companies',
                            successRemarks="Company deleted successfully!")
        if form.is_valid():
            company = {
                'username': request.POST.get('username'),
                'name_company': request.POST.get('name_company'),
                'email': request.POST.get('email'),
                'phone_number': request.POST.get('phone_number')
            }
            if request.POST.get('method') == 'insert':
                Company(date_created=date.today(), **company).save()
                return redirect('ezbook_admin:companies',
                                successRemarks="Company added successfully!")
            elif request.POST.get('method') == 'update':
                Company.objects.filter(
                    pk=request.POST.get('pk')).update(**company)
                return redirect('ezbook_admin:companies',
                                successRemarks="Company updated successfully!")
        companies = Company.objects.all()
        return render(request, 'ezbook_admin/tables/companies.html', {'title': f'{base_title} - {self.title}', 'companies': companies, 'form': form})


class Drivers(View):
    title = 'Drivers'

    def get(self, request, *args, **kwargs):
        form = DriverForm()
        drivers = Driver.objects.all()
        return render(request, 'ezbook_admin/tables/drivers.html', {'title': f'{base_title} - {self.title}', 'drivers': drivers, 'form': form, 'successRemarks': kwargs['successRemarks']})

    def post(self, request, *args, **kwargs):
        form = DriverForm(request.POST)
        if request.POST.get('method') == 'delete':
            Driver.objects.filter(pk=request.POST.get('pk')).delete()
            return redirect('ezbook_admin:drivers',
                            successRemarks="Driver deleted successfully!")
        if form.is_valid():
            driver = {
                'driver_fullname': request.POST.get('driver_fullname'),
                'company_name': Company.objects.get(id=request.POST.get('company_name'))
            }
            if request.POST.get('method') == 'insert':
                Driver(**driver).save()
                return redirect('ezbook_admin:drivers',
                                successRemarks="Driver added successfully!")
            elif request.POST.get('method') == 'update':
                Driver.objects.filter(
                    pk=request.POST.get('pk')).update(**driver)
                return redirect('ezbook_admin:drivers',
                                successRemarks="Driver updated successfully!")
        drivers = Driver.objects.all()
        return render(request, 'ezbook_admin/tables/drivers.html', {'title': f'{base_title} - {self.title}', 'drivers': drivers, 'form': form})


class Vehicles(View):
    title = 'Vehicles'

    def get(self, request, *args, **kwargs):
        form = VehicleForm()
        vehicles = Vehicle.objects.all()
        return render(request, 'ezbook_admin/tables/vehicles.html', {'title': f'{base_title} - {self.title}', 'vehicles': vehicles, 'form': form, 'successRemarks': kwargs['successRemarks']})

    def post(self, request, *args, **kwargs):
        form = VehicleForm(request.POST)
        if request.POST.get('method') == 'delete':
            Vehicle.objects.filter(pk=request.POST.get('pk')).delete()
            return redirect('ezbook_admin:vehicles',
                            successRemarks="Vehicle deleted successfully!")
        if form.is_valid():
            vehicle = {
                'vehicle_plate': request.POST.get('vehicle_plate'),
                'vehicle_driver_id': Driver.objects.get(id=request.POST.get('vehicle_driver_id')),
                'vehicle_capacity': request.POST.get('vehicle_capacity'),
                'vehicle_type': request.POST.get('vehicle_type'),
                'company_id': Company.objects.get(id=request.POST.get('company_id'))
            }
            if request.POST.get('method') == 'insert':
                Vehicle(**vehicle).save()
                return redirect('ezbook_admin:vehicles',
                                successRemarks="Vehicle added successfully!")
            elif request.POST.get('method') == 'update':
                Vehicle.objects.filter(
                    pk=request.POST.get('pk')).update(**vehicle)
                return redirect('ezbook_admin:vehicles',
                                successRemarks="Vehicle updated successfully!")
        vehicles = Vehicle.objects.all()
        return render(request, 'ezbook_admin/tables/vehicles.html', {'title': f'{base_title} - {self.title}', 'vehicles': vehicles, 'form': form})


class Travelplaces(View):
    title = 'Travel Places'

    def get(self, request, *args, **kwargs):
        form = Travel_PlacesForm()
        travel_places = Travel_Places.objects.all()
        return render(request, 'ezbook_admin/tables/travelplaces.html', {'title': f'{base_title} - {self.title}', 'travel_places': travel_places, 'form': form, 'successRemarks': kwargs['successRemarks']})

    def post(self, request, *args, **kwargs):
        form = Travel_PlacesForm(request.POST)
        if request.POST.get('method') == 'delete':
            Travel_Places.objects.filter(pk=request.POST.get('pk')).delete()
            return redirect('ezbook_admin:travelplaces',
                            successRemarks="Travel Place deleted successfully!")
        if form.is_valid():
            travel_place = {'places': request.POST.get('places')}
            if request.POST.get('method') == 'insert':
                Travel_Places(**travel_place).save()
                return redirect('ezbook_admin:travelplaces',
                                successRemarks="Travel Place added successfully!")
            elif request.POST.get('method') == 'update':
                Travel_Places.objects.filter(
                    pk=request.POST.get('pk')).update(**travel_place)
                return redirect('ezbook_admin:travelplaces',
                                successRemarks="Travel Place updated successfully!")
        travel_places = Travel_Places.objects.all()
        return render(request, 'ezbook_admin/tables/travelplaces.html', {'title': f'{base_title} - {self.title}', 'travel_places': travel_places, 'form': form})


class Bookings(View):
    title = 'Bookings'

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        bookings = Booking.objects.all()
        return render(request, 'ezbook_admin/tables/bookings.html', {'title': f'{base_title} - {self.title}', 'bookings': bookings, 'form': form, 'successRemarks': kwargs['successRemarks']})

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if request.POST.get('method') == 'delete':
            Booking.objects.filter(pk=request.POST.get('pk')).delete()
            return redirect('ezbook_admin:bookings',
                            successRemarks="Booking deleted successfully!")
        if form.is_valid():
            booking = {
                'seat_number': request.POST.get('seat_number'),
                'user_travel_id': User.objects.get(id=request.POST.get('user_travel_id')),
                'book_travel_id': BookTravel.objects.get(id=request.POST.get('book_travel_id'))
            }
            if request.POST.get('method') == 'insert':
                Booking(booking_date=date.today(), **booking).save()
                return redirect('ezbook_admin:bookings',
                                successRemarks="Booking added successfully!")
            elif request.POST.get('method') == 'update':
                Booking.objects.filter(
                    pk=request.POST.get('pk')).update(**booking)
                return redirect('ezbook_admin:bookings',
                                successRemarks="Booking updated successfully!")
        bookings = Booking.objects.all()
        return render(request, 'ezbook_admin/tables/bookings.html', {'title': f'{base_title} - {self.title}', 'bookings': bookings, 'form': form})


class Availablebookings(View):
    title = 'Available Bookings'

    def get(self, request, *args, **kwargs):
        form = BookTravelForm()
        available_bookings = BookTravel.objects.all()
        return render(request, 'ezbook_admin/tables/availablebookings.html', {'title': f'{base_title} - {self.title}', 'available_bookings': available_bookings, 'form': form, 'successRemarks': kwargs['successRemarks']})

    def post(self, request, *args, **kwargs):
        form = BookTravelForm(request.POST)
        if request.POST.get('method') == 'delete':
            BookTravel.objects.filter(pk=request.POST.get('pk')).delete()
            return redirect('ezbook_admin:availablebookings',
                            successRemarks="Booking Travel deleted successfully!")
        if form.is_valid():
            booktravel = {
                'vehicle_id': Vehicle.objects.get(id=request.POST.get('vehicle_id')),
                'place_from': Travel_Places.objects.get(id=request.POST.get('place_from')),
                'place_to': Travel_Places.objects.get(id=request.POST.get('place_to')),
                'available_travel_date': datetime.strptime(request.POST.get('available_travel_date'), "%Y-%m-%d").date(),
                'available_travel_time': datetime.strptime(':'.join(request.POST.get('available_travel_time').split(':', 2)[:2]), "%H:%M").time(),
                'company': Company.objects.get(id=request.POST.get('company'))
            }
            if request.POST.get('method') == 'insert':
                BookTravel(**booktravel).save()
                return redirect('ezbook_admin:availablebookings',
                                successRemarks="Booking Travel added successfully!")
            elif request.POST.get('method') == 'update':
                BookTravel.objects.filter(
                    pk=request.POST.get('pk')).update(**booktravel)
                return redirect('ezbook_admin:availablebookings',
                                successRemarks="Booking Travel updated successfully!")
        available_bookings = BookTravel.objects.all()
        return render(request, 'ezbook_admin/tables/availablebookings.html', {'title': f'{base_title} - {self.title}', 'available_bookings': available_bookings, 'form': form})
