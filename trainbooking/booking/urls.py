from django.urls import path
from booking.views import TicketBooking
urlpatterns = [
    path('user/bookings/', TicketBooking.as_view(), name="user-bookings"),
    path('user/book/ticket/', TicketBooking.as_view(), name='ticket-booking'),
]