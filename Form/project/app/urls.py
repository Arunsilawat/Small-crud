 
from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('userdata/', views.userdata, name='userdata'),
    path('profiledata/', views.profiledata, name='profiledata'),
    path('complatedata/', views.complatedata, name='complatedata'),
]