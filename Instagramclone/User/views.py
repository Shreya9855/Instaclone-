from django.shortcuts import render

from .form import SignUpForm

# Create your views here.
def signup(request):
    form = SignUpForm()
    return render(request,'signup.html',{"form": form})


def login(request):
    return render(request,'login.html' )


def profile(request):
    return render(request,'profile.html')
