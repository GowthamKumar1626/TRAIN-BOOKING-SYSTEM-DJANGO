from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from trains.models import Trains
from trains.serializers import TrainSerializer

class TrainView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        trains_list = Trains.objects.all()
        return Response(TrainSerializer(trains_list, many=True).data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        train_number = data.get('train_number')
        train_name = data.get('train_name')
        source = data.get('source')
        destination = data.get('destination')
        ticket_fare = data.get('ticket_fare')
        travel_path = data.get('travel_path')

        if not train_number or not train_name or not source or not destination or not ticket_fare:
            return Response({'detail': "Please give proper details"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            record = Trains.objects.create(
                train_number = train_number,
                train_name = train_name,
                source = source,
                destination = destination,
                ticket_fare = ticket_fare,
                travel_path = travel_path,
            )

            record.save()
        return Response(TrainSerializer(record).data, status=status.HTTP_200_OK)
    
    def patch(self, request):
        data = request.data
        
        train_number = data.get('train_number')
        train_name = data.get('train_name')
        source = data.get('source')
        destination = data.get('destination')
        ticket_fare = data.get('ticket_fare')
        travel_path = data.get('travel_path')

        if Trains.objects.filter(train_number = train_number).exists():

            record = Trains.objects.get(train_number=train_number)

            if train_name:
                record.train_name = train_name
            if source:
                record.source = source
            if destination:
                record.destination = destination
            if ticket_fare:
                record.ticket_fare = ticket_fare
            if travel_path:
                record.travel_path = travel_path
            record.save()
            return Response(TrainSerializer(record).data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': f'Train with {train_number} number is not exist'}, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request):
        
        data = request.data
        train_number = data.get('train_number')
        record = Trains.objects.get(train_number=train_number)
        record.delete()

        return Response({'details': f'Train with {train_number} is deleted'}, status=status.HTTP_204_NO_CONTENT)



class TrainSearchList(generics.ListAPIView):
    queryset = Trains.objects.all()
    serializer_class = TrainSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['train_name', 'train_number', 'ticket_fare', 'source', 'destination']