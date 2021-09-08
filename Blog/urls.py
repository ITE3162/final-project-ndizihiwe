from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name='blog'),
    path('blog-details/<int:bid>', blogdetails),
]
