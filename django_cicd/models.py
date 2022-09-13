from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Address(models.Model):
    street_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.street_name} {self.city.name}'


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
