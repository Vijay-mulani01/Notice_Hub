from django.contrib import admin
from django.urls import path
from User import views

urlpatterns = [
    path('notice', views.all_notices, name='notice'),
]