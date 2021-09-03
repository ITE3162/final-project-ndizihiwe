from django.shortcuts import render, redirect
from Dashboard.models import User, Blog
from django.contrib.auth.models import auth
from Dashboard.forms import BlogForms


# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['Firstname']
        last_name = request.POST['Lastname']
        username = request.POST['Username']
        email = request.POST['Email']
        photo = request.FILES['Photo']
        title = request.POST['Title']
        about = request.POST['About']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                print('Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                print('Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, username=username, password=password1,
                                                first_name=first_name, last_name=last_name, photo=photo, title=title,
                                                about=about)
                user.save()
                print('User created successfully')
                return redirect('login')
        else:
            print('Password not matching')
        return redirect('/')
    else:
        return render(request, "Dashboard/register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            print('Invalid credentials')
            return redirect('login')

    else:
        return render(request, "Dashboard/login.html")


def dashboard(request):
    return render(request, "Dashboard/Dashboard.html")


def create(request):
    if request.method == 'POST':
        if request.POST.get('Title') and request.POST.get('Genre') and request.POST.get(
                'Description') and request.FILES.get('Poster') and request.POST.get('Release'):
            saveblog = Blog()
            saveblog.Title = request.POST['Title']
            saveblog.Genre = request.POST['Genre']
            saveblog.Description = request.POST['Description']
            saveblog.Poster = request.FILES['Poster']
            saveblog.Release = request.POST['Release']
            saveblog.Author = request.user
            saveblog.save()
            print('Blog created successfully')
            return redirect('dashboard')
        else:
            print('Something went wrong')
            return redirect('create')
    return render(request, "Dashboard/create.html")


def bloglist(request):
    author = request.user
    context = Blog.objects.filter(Author=author)
    posts = {'posts': context}
    return render(request, "Dashboard/blog-list.html", posts)


def blogedit(request, eid):
    instance = Blog.objects.get(id=eid)
    editinfo = {'editinfo': instance}
    if request.method == "POST":
        form = BlogForms(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            print("Updated successfully")
            return redirect("blog-list")
        else:
            print("Couldn't update")
    return render(request, "Dashboard/blog-edit.html", editinfo)


def logout(request):
    auth.logout(request)
    return redirect('/')
