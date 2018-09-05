from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    lead_booker = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE, blank=True, null=True)


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookings = models.ManyToManyField('Booking', related_name='bookings', blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Status(models.Model): 
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    userType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


    





