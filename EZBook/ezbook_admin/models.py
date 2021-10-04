from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:
        db_table = "user"
    user_pic = models.CharField(
        max_length=100, default='noimage.png', null=False)
    username = models.CharField(max_length=100, default='', null=False)
    password = models.CharField(max_length=100, default='', null=False)
    firstname = models.CharField(max_length=100, default='', null=False)
    middlename = models.CharField(max_length=100, default='', null=False)
    lastname = models.CharField(max_length=100, default='', null=False)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=100, default='', null=False)
    email = models.EmailField()
    date_created = models.DateField()


class Company(models.Model):
    class Meta:
        db_table = "company"
    username = models.CharField(max_length=100, default='', null=False)
    password = models.CharField(max_length=100, default='', null=False)
    name_company = models.CharField(max_length=100, default='', null=False)
    date_created = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100, default='', null=False)
    company_pic = models.CharField(
        max_length=100, default='noimage.png', null=False)


class Driver(models.Model):
    class Meta:
        db_table = "driver"
    driver_pic = models.CharField(
        max_length=100, default='noimage.png', null=False)
    driver_fullname = models.CharField(max_length=100, default='', null=False)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)


class Vehicle(models.Model):
    class Meta:
        db_table = "vehicle"
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    vehicle_plate = models.CharField(max_length=100, default='', null=False)
    vehicle_driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle_capacity = models.IntegerField()
    vehicle_type = models.CharField(max_length=100, default='', null=False)
    vehicle_pic = models.CharField(
        max_length=100, default='noimage.png', null=False)


class Travel_Places(models.Model):
    class Meta:
        db_table = "travel_places"
    places = models.CharField(max_length=100, default='', null=False)


class BookTravel(models.Model):
    class Meta:
        db_table = "booktravel"
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    place_from = models.ForeignKey(
        Travel_Places, on_delete=models.CASCADE, related_name='places_from')
    place_to = models.ForeignKey(
        Travel_Places, on_delete=models.CASCADE, related_name='places_to')
    available_travel_date = models.DateField()
    available_travel_time = models.TimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Booking(models.Model):
    class Meta:
        db_table = "booking"
    booking_date = models.DateField()
    seat_number = models.IntegerField()
    user_travel_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_travel_id = models.ForeignKey(BookTravel, on_delete=models.CASCADE)
