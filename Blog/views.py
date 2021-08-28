from django.shortcuts import render
from Dashboard.models import Blog


# Create your views here.


def blog(request):
    context = Blog.objects.all()
    blogs = {'blogs': context}
    return render(request, "Blog/blog.html", blogs)


def blogdetails(request, bid):
    context = Blog.objects.filter(id=bid)
    details = {'details': context}
    return render(request, "Blog/blog-details.html", details)
