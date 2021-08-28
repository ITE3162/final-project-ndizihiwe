# from django.contrib.auth import login
from django.urls import path
from .views import Mainsite

urlpatterns = [
    path('', Mainsite, name='home'),
]
