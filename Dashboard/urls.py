from django.urls import path
from .views import register, login, logout, dashboard, create, bloglist, blogedit

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('Dashboard', dashboard, name='dashboard'),
    path('create', create, name='create'),
    path('blog-list', bloglist, name='blog-list'),
    path('edit-blog/<int:eid>', blogedit, name='edit-blog'),

]