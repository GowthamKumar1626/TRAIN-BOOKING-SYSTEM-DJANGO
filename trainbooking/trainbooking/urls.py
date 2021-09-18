from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('api/data/', include('booking.urls')),
    path('api/trains/', include('trains.urls')),
]
