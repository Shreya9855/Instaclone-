from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.home,name='home'),
    # path('add/',views.addPost,name='addPost'),
    # path('edit/<int:pk>/',views.editPost,name='editPost'),
    # path('delete/<int:pk>/',views.deletePost,name='deletePost'),
]
