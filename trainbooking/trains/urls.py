from django.urls import path
from django.conf.urls import url
from trains.views import TrainView, TrainSearchList

urlpatterns = [
    path('list/', TrainView.as_view(), name="trians-list"),
    path('create/', TrainView.as_view(), name="create-train"),
    path('update/', TrainView.as_view(), name="update-train"),
    path('delete/', TrainView.as_view(), name="delete-train"),
    url('^search/$',TrainSearchList.as_view(),name='Train-Search-List'),
]