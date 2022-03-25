from dataclasses import field
from django import forms
from User.models import UserModel

class SignUpForm(forms.ModelForm):
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

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'login_input',
                'name' : 'password',
                'type' : 'password',
            }
        )
    )

    class Meta:
        model = UserModel
        fields = ['display_name','username','email','password']