from django.db import models
from django.contrib.auth import get_user_model
from trains.models import Trains
import random

from datetime import date

today = date.today()

UserModel = get_user_model()

def booking_id_generator():
    return f"BI{random.randint(100000, 999999)}"

def get_booking_date():
    return today.strftime('%Y-%m-%d')

class Bookings(models.Model):
    class Meta:
        verbose_name_plural = "Bookings"
        ordering = ('booking_date', )

    booking_id = models.CharField(max_length=8, primary_key=True, default=booking_id_generator)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    train_id = models.ForeignKey(Trains, on_delete=models.CASCADE)
    date_of_journey = models.CharField(max_length=20, default=get_booking_date)
    booking_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.booking_id

class BookingStatus(models.Model):
    class Meta:
        verbose_name_plural = "BookingStatus"
        ordering = ('user',)
    
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    last_booking = models.DateField(auto_now=True)    