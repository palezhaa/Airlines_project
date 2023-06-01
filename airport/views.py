from django.db.models import Value, CharField, F
from django.db.models.functions import Concat
from django.shortcuts import render, redirect

from airport.models import City, ShedFlight


def index(request):
    if request.method == 'GET':
        from_city = request.GET.get('from')
        to_city = request.GET.get('to')
        departure_date = request.GET.get('departure')

        if from_city and to_city and departure_date:
            return redirect('search_flights', from_city=from_city, to_city=to_city, departure_date=departure_date)

    return render(request, 'index.html')


def search(request, from_city, to_city, departure_date):
    # shed_flight_data = ShedFlight.objects.all().select_related('flight_nbr').values(
    #     'flight_date',
    #     'flight_nbr__depart_code',
    #     'flight_nbr__ariv_code',
    #     'seat_ava',
    #     'tod',
    #     'toa',
    #     'serial',
    #     'cost'
    # ).filter(flight_nbr__depart_code__city_code__city_name=from_city).annotate(
    #     city_name=F('flight_nbr__depart_code__city_code__city_name')).values('flight_date', 'flight_nbr', 'seat_ava',
    #                                                                          'tod', 'toa', 'serial',
    #                                                                          'flight_nbr__ariv_code',
    #                                                                          'flight_nbr__depart_code', 'cost',
    #                                                                          'city_name')
    shed_flight_qs = ShedFlight.objects.filter(
        flight_nbr__depart_code__city_code__city_name=from_city, flight_date=departure_date
    ).annotate(
        city_name=F('flight_nbr__depart_code__city_code__city_name')
    ).values(
        'flight_date', 'flight_nbr', 'seat_ava', 'tod', 'toa', 'serial', 'flight_nbr__ariv_code',
        'flight_nbr__depart_code', 'cost', 'city_name'
    )

    if len(shed_flight_qs) > 0:
        return render(request, 'search_flights.html', {'flight_data': shed_flight_qs})
    return render(request, 'not_found.html')


def city_list(request):
    cities = City.objects.all()
    print(cities)
    return render(request, 'city_list.html', {'cities': cities})
