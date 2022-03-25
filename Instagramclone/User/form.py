from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from User.models import UserModel

class CustomUserCreationForm(UserCreationForm):
    display_name = forms.CharField(
        required = True,
        widget= forms.TextInput(
            attrs = {
                'class' : 'login_input',
                'placeholder' : 'Name',
                'name' : 'display_name',
                'type' : 'text',
            }
        )
    )
    username = forms.CharField(
        required=True,
        widget= forms.TextInput(
            attrs = {
                'class' : 'login_input',
                'placeholder' : 'Username',
                'name' : 'username',
                'type' : 'text' ,

            }
        )
    )
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(
            attrs = {
                'class' : 'login_input',
                'placeholder' : 'Email',
                'name': 'email',
                'type' :'text',
            }
        )
    )

    class Meta:
        model = UserModel
        fields = ('display_name','username','email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('username','email')

    