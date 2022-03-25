from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import UserModel

# Register your models here.

class CustomUSerAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserModel
    list_display = ['email', 'username']

admin.site.register(UserModel,CustomUSerAdmin)

