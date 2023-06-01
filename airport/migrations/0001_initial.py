# Generated by Django 4.2.1 on 2023-05-08 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftData',
            fields=[
                ('type', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
                ('capacity', models.CharField(max_length=3)),
                ('range', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('serial', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.aircraftdata')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_nbr', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='FlightData',
            fields=[
                ('flight_nbr', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('ariv_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='airport.airport')),
                ('depart_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='airport.airport')),
            ],
        ),
        migrations.CreateModel(
            name='ShedFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_date', models.DateField()),
                ('seats_resvd', models.CharField(max_length=3)),
                ('seat_ava', models.CharField(max_length=3)),
                ('tod', models.CharField(max_length=8)),
                ('toa', models.CharField(max_length=8)),
                ('flight_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.flightdata')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.aircrafttype')),
            ],
            options={
                'unique_together': {('flight_date', 'flight_nbr')},
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_date', models.DateField()),
                ('cust_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.customer')),
                ('flight_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.shedflight')),
            ],
        ),
        migrations.AddField(
            model_name='airport',
            name='city_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.city'),
        ),
    ]
