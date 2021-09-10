from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('Dashboard', dashboard, name='dashboard'),
    path('create', create, name='create'),
    path('blog-list', bloglist, name='blog-list'),
    path('edit-blog/<int:eid>', blogedit, name='edit-blog'),
    path('delete-blog/<int:eid>', blogdelete, name='delete-blog'),

]