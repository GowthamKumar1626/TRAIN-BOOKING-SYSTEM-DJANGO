from django.db.models import fields
from rest_framework import serializers
from booking.models import Bookings, BookingStatus

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = "__all__"

class BookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingSerializer
        fields = "__all__"