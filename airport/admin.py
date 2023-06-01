from django.contrib import admin

from airport.models import ShedFlight, AircraftData, AircraftType, City, Airport, FlightData, Reservation, Customer


# Register your models here.

class ShedFlightAdmin(admin.ModelAdmin):
    list_display = ['flight_nbr', 'flight_date', 'seats_resvd', 'seat_ava', 'tod', 'toa', 'serial', 'cost']


class AircraftDataAdmin(admin.ModelAdmin):
    list_display = ['type', 'description', 'capacity', 'range']


class AircraftTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'serial']


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'state', 'city_code']


class AirportAdmin(admin.ModelAdmin):
    list_display = ['city_code', 'airport_name', 'airport_code']


class FlightDataAdmin(admin.ModelAdmin):
    list_display = ['depart_code', 'ariv_code', 'flight_nbr']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['cust_nbr', 'flight_nbr', 'flight_date']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cust_nbr', 'cust_name']


admin.site.register(ShedFlight, ShedFlightAdmin)
admin.site.register(AircraftData, AircraftDataAdmin)
admin.site.register(AircraftType, AircraftTypeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(FlightData, FlightDataAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Customer, CustomerAdmin)
