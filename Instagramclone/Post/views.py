from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from User.models import UserModel

from .forms import newProfileForm

# Create your views here.
def home(request):
    return render(request,'home.html')


  

@login_required
def profile(request):
    current_user = request.user
    id =  current_user.id
    print(id)
    get_profile = UserModel.objects.filter(id=id)
    print(get_profile)
    if get_profile:
        form = newProfileForm(request.POST,get_profile)
    #     if form.is_valid():
    #         email = form['email']
    #         profile_pic = form['profile_pic']
    #         bio = form['bio']
    #         website = form['website']
    #         reg = UserModel(profile_pic=profile_pic, email=email, bio=bio, website=website)
    #         reg.save()
    #         return redirect('home')

    return render(request, 'profile.html',{form:form})