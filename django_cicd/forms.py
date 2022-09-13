from django.forms import ModelForm
from .models import *


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
