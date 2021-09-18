from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from booking.serializers import BookingSerializer, BookingStatusSerializer
from booking.models import Bookings, BookingStatus
from trains.models import Trains

from datetime import date

today = date.today()

class TicketBooking(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            booking_record = Bookings.objects.filter(user_id=user).all()
            data = BookingSerializer(booking_record, many=True).data
            if len(data) == 0:
                return Response({'detail': 'You have no previous bookings'}, status=status.HTTP_204_NO_CONTENT)       
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'Error occured. Please Try again'}, status=status.HTTP_400_BAD_REQUEST)      

    def post(self, request):
        user = request.user
        try:
            data = request.data
            train_number = data.get('train_number')
            date_of_journey = data.get('date_of_journey')
            booking_status = BookingStatus.objects.get(user=user)
            if Trains.objects.filter(train_number=train_number).exists():
                train_record = Trains.objects.get(train_number=train_number)
                if booking_status.status:
                    if date_of_journey:
                        booking_record = Bookings.objects.create(user_id=user,  train_id=train_record, date_of_journey=date_of_journey)
                        serializer = BookingSerializer(booking_record)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                         return Response({'detail': 'Please enter your date of journey in format YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    if('2021-09-22' < today.strftime('%Y-%m-%d')):
                        
                        booking_record = Bookings.objects.create(user_id=user,  train_id=train_record)
                        serializer = BookingSerializer(booking_record)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:   
                        return Response({'detail': 'Sorry please try after 24hrs from your last booking date'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': f"Train with {train_number} number does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'detail': str(error)}, status=status.HTTP_400_BAD_REQUEST) 