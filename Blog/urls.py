from django.urls import path
from .views import blog, blogdetails

urlpatterns = [
    path('', blog, name='blog'),
    path('blog-details/<int:bid>', blogdetails),
]
