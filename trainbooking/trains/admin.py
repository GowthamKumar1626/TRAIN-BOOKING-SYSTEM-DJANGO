from django.contrib import admin
from trains.models import Trains

class TrainAdmin(admin.ModelAdmin):
    model = Trains
    list_display = ["train_number", "source", "destination", "ticket_fare"]

admin.site.register(Trains, TrainAdmin)