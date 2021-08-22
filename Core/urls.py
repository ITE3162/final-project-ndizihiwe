# from django.contrib.auth import login
from django.urls import path
from .views import Mainsite, register, login, dashboard, create, bloglist

urlpatterns = [
    path('', Mainsite, name='home'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('create', create, name='create'),
    path('blog-list', bloglist, name='blog-list'),
]
