from django.urls import path
from base.views import get_all_users, MyTokenObtainPairView, getUserProfile, registerUser, updateUserProfile

urlpatterns = [
    path('auth/login/', MyTokenObtainPairView.as_view(), name='user-login'),
    path('auth/register/', registerUser, name='user-register'),
    path('users/', get_all_users, name="get-all-users"),
    path('users/profile/', getUserProfile, name='user-profile'),
    path('users/profile/update/', updateUserProfile, name='user-profile-update'),
]