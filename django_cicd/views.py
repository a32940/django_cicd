from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *


def person(request):
    if request.method == "POST":
        return HttpResponse("POST")
    else:
        form = PersonForm()
        return render(request, "person/person.html", {'form': form})


def address(request):
    if request.method == "POST":
        return HttpResponse("POST")
    else:
        form = AddressForm()
        return render(request, "address/address.html", {'form': form})


def city(request):
    if request.method == "POST":
        return HttpResponse("POST")
    else:
        form = CityForm()
        return render(request, "city/city.html", {'form': form})


def country(request):
    if request.method == "POST":
        return HttpResponse("POST")
    else:
        form = CountryForm()
        return render(request, "country/country.html", {'form': form})
