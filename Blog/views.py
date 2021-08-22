from django.shortcuts import render


# Create your views here.

def blog(request):
    return render(request, "Blog/blog.html")


def blogdetails(request):
    return render(request, "Blog/blog-details.html")
