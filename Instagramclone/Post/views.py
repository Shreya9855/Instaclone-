from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import newProfileForm

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = newProfileForm(request.POST)
        if form.is_valid():
            # process form data
            form.save()
            return HttpResponseRedirect('Profile updated')

    else:
        form = newProfileForm()

    return render(request, 'profile.html', {'form': form})