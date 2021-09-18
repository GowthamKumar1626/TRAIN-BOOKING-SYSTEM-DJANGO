from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ["username", "email", "is_staff", "mobile_number"]

admin.site.register(UserModel, CustomUserAdmin)