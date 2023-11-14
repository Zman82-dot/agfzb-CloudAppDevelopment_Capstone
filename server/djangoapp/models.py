import datetime
from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=True, max_length=500)

def __str__(self):
    return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)
    dealer_id = models.IntegerField(null=True)

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    SPORT = "Sport"
    COUPE = "Coupe"
    MINIVAN = "Mini"
    VAN = "Van"
    PICKUP = "Pickup"
    TRUCK = "Truck"
    BIKE = "Bike"
    SCOOTER = "Scooter"
    OTHER = "Other"
    CAR_CHOICES = [(SEDAN,"Sedan"), (SUV, "SUV"), (WAGON,"Wagon"),(SPORT,"Sports Car"),
                   (COUPE,"Coupe"),(MINIVAN, "Minivan"), (VAN,"Van"),(PICKUP,"Pick-up truck"),
                   (TRUCK,"Truck"),(BIKE,"motor bike"),(SCOOTER,"Scooter"), (OTHER,'Other')]
    model_type = models.CharField(
        null=False, max_length=15, choices=CAR_CHOICES, default=SEDAN)

    YEAR_CHOICES =[]
    for r in range(1969,(datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    year = models.IntegerField(
        ('year'),choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return f"{self.year} {self.car_make.name} {self.name} "




class CarDealer:

    def __init__(self, id, city, state, st, address, zip, lat, long, short_name, full_name):
        self.id = id
        self.city = city
        self.state=state
        self.st=st
        self.address = address
        self.zip = zip
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name


class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year,sentiment, id):
        self.dealership=dealership
        self.name=name
        self.purchase=purchase
        self.review=review
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=car_year
        self.sentiment=sentiment #Watson NLU service
        self.id=id

    def __str__(self):
        return "Review: " + self.review +\
                " Sentiment: " + self.sentiment 