from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import UserModel
# from django.views.generic.edit import CreateView
from .form import CustomUserCreationForm


# Create your views here.
def signup(request):
    print(request)
    if request == 'POST':
        print('halfdelayasfa')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(' upload successful')
        # return redirect('login')     
    else:
        form = CustomUserCreationForm()
        print("You ARE NOT signed in") 
       
    return render(request,'signup.html',{"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = UserModel.objects.filter(username = username,password=password).first()
        print(user)
        if not user:
            return redirect('login')
        else:
            return redirect('home')

    return render(request,'login.html' )

def logout(request):
    logout(request)
    print(request, "Logged out successfully!")
    return redirect('home.html')



def profile(request):
    return render(request,'profile.html')
