from django.shortcuts import render
from django.views.generic import View
from ezbook_admin.models import User, Company, Driver, Vehicle, Travel_Places, BookTravel, Booking
from ezbook_admin.forms import UserForm, CompanyForm, DriverForm, VehicleForm, Travel_PlacesForm, BookTravelForm, BookingForm
from datetime import date, datetime
import json
from django.core.serializers.json import DjangoJSONEncoder

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

    return render(request, 'ezbook_admin/index.html', {'title': f'{base_title} - Dashboard', 'count': count, 'date': json.dumps(date, cls=DjangoJSONEncoder), 'num': json.dumps(num)})


class Users(View):
    title = 'Users'

    def get(self, request):
        form = UserForm()
        users = User.objects.all()
        return render(request, 'ezbook_admin/tables/users.html', {'title': f'{base_title} - {self.title}', 'users': users, 'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        isSuccess = False
        if form.is_valid():
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            middlename = request.POST.get('middlename')
            lastname = request.POST.get('lastname')
            age = request.POST.get('age')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            user = User(
                username=username,
                firstname=firstname,
                middlename=middlename,
                lastname=lastname,
                age=age,
                phone_number=phone_number,
                email=email,
                date_created=date.today()
            )
            user.save()
            form = UserForm()
            isSuccess = True
        users = User.objects.all()
        return render(request, 'ezbook_admin/tables/users.html', {'title': f'{base_title} - {self.title}', 'users': users, 'form': form, 'isSuccess': isSuccess})


class Companies(View):
    title = 'Companies'

    def get(self, request):
        form = CompanyForm()
        companies = Company.objects.all()
        return render(request, 'ezbook_admin/tables/companies.html', {'title': f'{base_title} - {self.title}', 'companies': companies, 'form': form})

    def post(self, request):
        form = CompanyForm(request.POST)
        isSuccess = False
        if form.is_valid():
            username = request.POST.get('username')
            name_company = request.POST.get('name_company')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            companies = Company(
                username=username,
                name_company=name_company,
                phone_number=phone_number,
                email=email,
                date_created=date.today()
            )
            companies.save()
            form = CompanyForm()
            isSuccess = True
        companies = Company.objects.all()
        return render(request, 'ezbook_admin/tables/companies.html', {'title': f'{base_title} - {self.title}', 'companies': companies, 'form': form, 'isSuccess': isSuccess})


class Drivers(View):
    title = 'Drivers'

    def get(self, request):
        form = DriverForm()
        drivers = Driver.objects.all()
        return render(request, 'ezbook_admin/tables/drivers.html', {'title': f'{base_title} - {self.title}', 'drivers': drivers, 'form': form})

    def post(self, request):
        form = DriverForm(request.POST)
        isSuccess = False
        if form.is_valid():
            driver_fullname = request.POST.get('driver_fullname')
            company_name = request.POST.get('company_name')
            drivers = Driver(
                driver_fullname=driver_fullname,
                company_name=Company.objects.get(id=company_name)
            )
            drivers.save()
            form = DriverForm()
            isSuccess = True
        drivers = Driver.objects.all()
        return render(request, 'ezbook_admin/tables/drivers.html', {'title': f'{base_title} - {self.title}', 'drivers': drivers, 'form': form, 'isSuccess': isSuccess})


class Vehicles(View):
    title = 'Vehicles'

    def get(self, request):
        form = VehicleForm()
        vehicles = Vehicle.objects.all()
        return render(request, 'ezbook_admin/tables/vehicles.html', {'title': f'{base_title} - {self.title}', 'vehicles': vehicles, 'form': form})

    def post(self, request):
        form = VehicleForm(request.POST)
        isSuccess = False
        if form.is_valid():
            vehicle_plate = request.POST.get('vehicle_plate')
            vehicle_driver_id = request.POST.get('vehicle_driver_id')
            vehicle_capacity = request.POST.get('vehicle_capacity')
            vehicle_type = request.POST.get('vehicle_type')
            company_id = request.POST.get('company_id')
            vehicles = Vehicle(
                vehicle_plate=vehicle_plate,
                vehicle_driver_id=Driver.objects.get(id=vehicle_driver_id),
                vehicle_capacity=vehicle_capacity,
                vehicle_type=vehicle_type,
                company_id=Company.objects.get(id=company_id)
            )
            vehicles.save()
            form = VehicleForm()
            isSuccess = True
        vehicles = Vehicle.objects.all()
        return render(request, 'ezbook_admin/tables/vehicles.html', {'title': f'{base_title} - {self.title}', 'vehicles': vehicles, 'form': form, 'isSuccess': isSuccess})


class Travelplaces(View):
    title = 'Travel Places'

    def get(self, request):
        form = Travel_PlacesForm()
        travel_places = Travel_Places.objects.all()
        return render(request, 'ezbook_admin/tables/travelplaces.html', {'title': f'{base_title} - {self.title}', 'travel_places': travel_places, 'form': form})

    def post(self, request):
        form = Travel_PlacesForm(request.POST)
        isSuccess = False
        if form.is_valid():
            places = request.POST.get('places')
            travel_places = Travel_Places(
                places=places
            )
            travel_places.save()
            form = Travel_PlacesForm()
            isSuccess = True
        travel_places = Travel_Places.objects.all()
        return render(request, 'ezbook_admin/tables/travelplaces.html', {'title': f'{base_title} - {self.title}', 'travel_places': travel_places, 'form': form, 'isSuccess': isSuccess})


class Bookings(View):
    title = 'Bookings'

    def get(self, request):
        form = BookingForm()
        bookings = Booking.objects.all()
        return render(request, 'ezbook_admin/tables/bookings.html', {'title': f'{base_title} - {self.title}', 'bookings': bookings, 'form': form})

    def post(self, request):
        form = BookingForm(request.POST)
        isSuccess = False
        if form.is_valid():
            booking_date = request.POST.get('booking_date')
            seat_number = request.POST.get('seat_number')
            user_travel_id = request.POST.get('user_travel_id')
            book_travel_id = request.POST.get('book_travel_id')
            bookings = Booking(
                seat_number=seat_number,
                user_travel_id=User.objects.get(id=user_travel_id),
                book_travel_id=BookTravel.objects.get(id=book_travel_id),
                booking_date=date.today()
            )
            bookings.save()
            form = BookingForm()
            isSuccess = True
        bookings = Booking.objects.all()
        return render(request, 'ezbook_admin/tables/bookings.html', {'title': f'{base_title} - {self.title}', 'bookings': bookings, 'form': form, 'isSuccess': isSuccess})


class Availablebookings(View):
    title = 'Available Bookings'

    def get(self, request):
        form = BookTravelForm()
        available_bookings = BookTravel.objects.all()
        return render(request, 'ezbook_admin/tables/availablebookings.html', {'title': f'{base_title} - {self.title}', 'available_bookings': available_bookings, 'form': form})

    def post(self, request):
        form = BookTravelForm(request.POST)
        isSuccess = False
        if form.is_valid():
            vehicle_id = request.POST.get('vehicle_id')
            place_from = request.POST.get('place_from')
            place_to = request.POST.get('place_to')
            available_travel_date = request.POST.get('available_travel_date')
            available_travel_time = request.POST.get('available_travel_time')
            company = request.POST.get('company')
            available_bookings = BookTravel(
                vehicle_id=Vehicle.objects.get(id=vehicle_id),
                place_from=Travel_Places.objects.get(id=place_from),
                place_to=Travel_Places.objects.get(id=place_to),
                available_travel_date=datetime.strptime(
                    available_travel_date, "%Y-%m-%d").date(),
                available_travel_time=datetime.strptime(
                    available_travel_time, "%H:%M").time(),
                company=Company.objects.get(id=company)
            )
            available_bookings.save()
            form = BookTravelForm()
            isSuccess = True
        available_bookings = BookTravel.objects.all()
        return render(request, 'ezbook_admin/tables/availablebookings.html', {'title': f'{base_title} - {self.title}', 'available_bookings': available_bookings, 'form': form, 'isSuccess': isSuccess})
