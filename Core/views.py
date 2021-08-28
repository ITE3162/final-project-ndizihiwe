from django.shortcuts import render


# Create your views here.
def Mainsite(request):
    return render(request, "Core/index.html")


