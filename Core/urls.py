
from django.urls import path
from .views import Mainsite

urlpatterns = [
    path('', Mainsite, name='Home'),
    path('/Register', register, name='Register'),
]