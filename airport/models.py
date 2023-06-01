from django.db import models


class City(models.Model):
    city_code = models.CharField(max_length=3, primary_key=True)
    city_name = models.CharField(max_length=15)
    state = models.CharField(max_length=2)

    class Meta:
        db_table = "City"


class AircraftData(models.Model):
    class Meta:
        db_table = "AIRCRAFT_DATA"

    type = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=20)
    capacity = models.CharField(max_length=3)
    range = models.CharField(max_length=4)


class AircraftType(models.Model):
    class Meta:
        db_table = "AIRCRAFT_TYPE"

    serial = models.CharField(max_length=8, primary_key=True, db_column='serial')
    type = models.ForeignKey(AircraftData, on_delete=models.CASCADE, db_column='type')


class Airport(models.Model):
    class Meta:
        db_table = "Airport"

    airport_code = models.CharField(max_length=7, primary_key=True)
    city_code = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_code')
    airport_name = models.CharField(max_length=30)


class FlightData(models.Model):
    class Meta:
        db_table = "FLIGHTDATA"

    flight_nbr = models.CharField(max_length=3, primary_key=True)
    depart_code = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE, db_column='depart_code')
    ariv_code = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE, db_column='ariv_code')


class ShedFlight(models.Model):
    flight_date = models.DateField()
    flight_nbr = models.ForeignKey(FlightData, on_delete=models.CASCADE, db_column='flight_nbr')
    seats_resvd = models.CharField(max_length=3)
    seat_ava = models.CharField(max_length=3)
    tod = models.CharField(max_length=8)
    toa = models.CharField(max_length=8)
    serial = models.ForeignKey(AircraftType, on_delete=models.CASCADE, db_column='serial')
    cost = models.DecimalField(max_digits=10, decimal_places=2, db_column='cost')
    class Meta:
        db_table = "SHED_FLIGHT"
        unique_together = (('flight_date', 'flight_nbr'),)


class Customer(models.Model):
    class Meta:
        db_table = "Customer"

    cust_nbr = models.CharField(max_length=3, primary_key=True)
    cust_name = models.CharField(max_length=15)


class Reservation(models.Model):
    class Meta:
        db_table = "Reservation"

    cust_nbr = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='cust_nbr')
    flight_nbr = models.ForeignKey(ShedFlight, on_delete=models.CASCADE, db_column='flight_nbr')
    flight_date = models.DateField()
