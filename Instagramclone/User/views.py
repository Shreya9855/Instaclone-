from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import UserModel
from django.views.generic.edit import CreateView
from .form import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name ='signup.html'

    def signup(request):    
        if request == 'POST':    
            form = CustomUserCreationForm(request.POST.get)   
            if form.is_valid():
                print(request.POST['id'])
                form.save()
            return redirect('login')     
        else:
            form = CustomUserCreationForm()
        return render(request,'signup.html',{"form": form})





# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = UserModel.objects.filter(username = username,password=password).first()
#         print(user)
#         if not user:
#             return redirect('login')
#         else:
#             return redirect('home')

#     return render(request,'login.html' )

# def logout(request):
#     logout(request)
#     print(request, "Logged out successfully!")
#     return redirect('home.html')



