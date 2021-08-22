from django.shortcuts import render


# Create your views here.
def Mainsite(request):
    return render(request, "Core/index.html")


def register(request):
    return render(request, "Core/register.html")


def login(request):
    return render(request, "Core/login.html")


def dashboard(request):
    return render(request, "Core/dashboard.html")


def create(request):
    return render(request, "Core/create.html")


def bloglist(request):
    return render(request, "Core/blog-list.html")
