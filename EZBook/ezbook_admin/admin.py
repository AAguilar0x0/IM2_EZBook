from django.contrib import admin
from ezbook_admin.models import User, Company, Driver, Vehicle, Travel_Places, BookTravel, Booking

# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Travel_Places)
admin.site.register(BookTravel)
admin.site.register(Booking)
