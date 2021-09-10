from django.contrib import messages
from django.shortcuts import render, redirect
from Core.models import About, Service, Contact
from Dashboard.models import Blog, User


# Create your views here.
def Mainsite(request):
    about = About.objects.all()
    services = Service.objects.all()
    users = User.objects.all().exclude(is_superuser=True)
    blogs = Blog.objects.all()[:3]
    data = {'about': about, 'services': services, 'team': users, 'posts': blogs, }
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('subject') and request.POST.get(
                'message'):
            savemessage = Contact()
            savemessage.Email = request.POST['email']
            savemessage.Subject = request.POST['subject']
            savemessage.Message = request.POST['message']
            savemessage.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
        else:
            print('Something went wrong')
            return redirect('home')
    return render(request, "Core/index.html", data)
