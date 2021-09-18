from django.contrib import admin
from booking.models import Bookings
from booking.models import BookingStatus

class BookingAdmin(admin.ModelAdmin):
    model = Bookings
    list_display = ['booking_id', 'booking_date', 'user_id', 'train_id']

admin.site.register(Bookings, BookingAdmin)

class BookingStatusAdmin(admin.ModelAdmin):
    model = BookingStatus
    list_display = ["user", "status", "last_booking"]

admin.site.register(BookingStatus, BookingStatusAdmin)