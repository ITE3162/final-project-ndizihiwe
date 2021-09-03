from django.shortcuts import render
from Core.models import About, Service
from Dashboard.models import Blog, User


# Create your views here.
def Mainsite(request):
    about = About.objects.all()
    services = Service.objects.all()
    users = User.objects.all().exclude(is_superuser=True)
    blogs = Blog.objects.all()[:3]
    data = {'about': about, 'services': services, 'team': users, 'posts': blogs, }
    return render(request, "Core/index.html", data)
