from django.urls import path
from django.contrib import admin
from lists import views

urlpatterns = [
  # url(regex, view)
  path('', views.home_page, name='home'),
]
