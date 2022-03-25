from . import views
from .views import SignUpView
from django.urls import  path

urlpatterns = [
    # path('login/',views.login,name = "login"),
    path("signup/",SignUpView.as_view(),name = 'signup'),
    path('profile/',views.profile,name='profile.html')
]


