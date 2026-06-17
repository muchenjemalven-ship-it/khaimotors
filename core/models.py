from django.db import models


class Vehicle(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    description = models.TextField(blank=True)
    year = models.IntegerField(default=2020)

    def __str__(self):
        return self.title


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='vehicles/')

    def __str__(self):
        return self.vehicle.title


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name