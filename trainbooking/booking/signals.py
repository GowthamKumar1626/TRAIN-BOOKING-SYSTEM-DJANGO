from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from booking.models import Bookings, BookingStatus

UserModel = get_user_model()

def create_booking_status(sender, instance, created, **kwargs):
    if created:
        user_record = UserModel.objects.get(username=instance.username)
        if not BookingStatus.objects.filter(user=user_record).exists():
            record = BookingStatus.objects.create(user=user_record)
            record.save()
    
    print('Signal triggered booking instance created')
post_save.connect(create_booking_status, UserModel)

def update_booking_status(sender, instance, created, **kwargs):
    if created:
        user_record = UserModel.objects.get(username=instance.user_id)
        if BookingStatus.objects.filter(user=user_record).exists():
            record = BookingStatus.objects.get(user=user_record)
            
            if record.status == True:
                record.status = False
                record.save()
                print('Signal triggered')
                
post_save.connect(update_booking_status, Bookings)