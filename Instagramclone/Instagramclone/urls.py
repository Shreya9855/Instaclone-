from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('',include('Post.urls')),
]
