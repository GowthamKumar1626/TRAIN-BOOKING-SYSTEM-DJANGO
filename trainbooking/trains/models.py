from django.db import models
import random

def generate_train_number():
    return random.randint(100000, 999999)

class Trains(models.Model):
    class Meta:
        verbose_name_plural = 'Trains'
        ordering = ('train_number',)

    train_number = models.CharField(primary_key=True, max_length=10, default=generate_train_number)
    train_name = models.CharField(unique=True, max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    destination = models.CharField(max_length=100, null=True, blank=True)
    ticket_fare = models.IntegerField(null=True, blank=True)
    travel_path = models.TextField(default=list)

    def __str__(self):
        return self.train_name