from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('user/',include('django.contrib.auth.urls')),
    path('',include('Post.urls')),
]
