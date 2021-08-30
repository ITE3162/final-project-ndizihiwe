from django.shortcuts import render
from Dashboard.models import Blog, User


# Create your views here.


def blog(request):
    context = Blog.objects.all()
    blogs = {'blogs': context}
    return render(request, "Blog/blog.html", blogs)


def blogdetails(request, bid):
    context = Blog.objects.get(id=bid)
    Ge = context.Genre
    context2 = Blog.objects.filter(Genre=Ge).exclude(id=bid)
    both = {'related': context2, 'details': context}
    return render(request, "Blog/blog-details.html", both)
